from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.exercise import Exercise
    from app.models.set import Set
    from app.models.workout_session import WorkoutSession


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid4
    )
    workout_session_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("workout_sessions.id"), nullable=False
    )
    exercise_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("exercises.id"), nullable=False
    )
    position: Mapped[int] = mapped_column(nullable=False)

    workout_session: Mapped[WorkoutSession] = relationship(
        back_populates="workout_exercises"
    )
    exercise: Mapped[Exercise] = relationship(back_populates="workout_exercises")
    sets: Mapped[list[Set]] = relationship(
        back_populates="workout_exercise",
        cascade="all, delete-orphan",
        order_by="Set.order",
    )
