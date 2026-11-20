from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.routine_exercise import RoutineExercise
    from app.models.user import User
    from app.models.workout_session import WorkoutSession


class Routine(Base):
    __tablename__ = "routines"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(100))

    user: Mapped[User] = relationship(back_populates="routines")
    routine_exercises: Mapped[list[RoutineExercise]] = relationship(
        back_populates="routine",
        cascade="all, delete-orphan",
        order_by="RoutineExercise.order",
    )
    workouts: Mapped[list[WorkoutSession]] = relationship(back_populates="routine")
