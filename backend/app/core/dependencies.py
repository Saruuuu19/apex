from datetime import UTC, datetime
from hashlib import sha256
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyCookie
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.auth_session import AuthSession
from app.models.user import User

session_cookie = APIKeyCookie(name="session", auto_error=False)


def credentials_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired session.",
        headers={"WWW-Authenticate": "APIKey"},
    )


def get_current_session(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str | None, Depends(session_cookie)],
) -> AuthSession:
    if not token:
        raise credentials_exception()

    session = db.get(AuthSession, sha256(token.encode()).hexdigest())
    if session is None or session.expires_at <= datetime.now(UTC).replace(tzinfo=None):
        raise credentials_exception()
    return session


def get_current_user(
    db: Annotated[Session, Depends(get_db)],
    session: Annotated[AuthSession, Depends(get_current_session)],
) -> User:
    user = db.get(User, session.user_id)
    if user is None:
        raise credentials_exception()
    return user
