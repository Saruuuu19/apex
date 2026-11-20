from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.exercise import Exercise
    from app.models.routine import Routine
    from app.models.set import Set


class RoutineExercise(Base):
    __tablename__ = "routine_exercises"
    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid4
    )
    routine_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("routines.id"), nullable=False
    )
    exercise_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("exercises.id"), nullable=False
    )
    order: Mapped[int] = mapped_column(nullable=False)

    routine: Mapped[Routine] = relationship(back_populates="routine_exercises")
    exercise: Mapped[Exercise] = relationship(back_populates="routine_exercises")
    sets: Mapped[list[Set]] = relationship(
        back_populates="routine_exercise",
        cascade="all, delete-orphan",
        order_by="Set.order",
    )
