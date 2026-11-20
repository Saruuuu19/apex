from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.schemas.types import UsernameStr


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: UsernameStr
    email: str
    created_at: datetime

class UserUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: UsernameStr
