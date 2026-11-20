from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.routine import Routine
    from app.models.user import User
    from app.models.workout_exercise import WorkoutExercise


class WorkoutSession(Base):
    __tablename__ = "workout_sessions"

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid4
    )
    user_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    routine_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("routines.id"), nullable=True
    )
    started_at: Mapped[datetime] = mapped_column(
        DateTime(), default=lambda: datetime.now(UTC)
    )  # Pendiente
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable=True)

    user: Mapped[User] = relationship(back_populates="workout_sessions")
    routine: Mapped[Routine | None] = relationship(back_populates="workouts")
    workout_exercises: Mapped[list[WorkoutExercise]] = relationship(
        back_populates="workout_session",
        cascade="all, delete-orphan",
        order_by="WorkoutExercise.position",
    )
