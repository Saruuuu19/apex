from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, ForeignKey, Numeric, Uuid
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import SetType

if TYPE_CHECKING:
    from app.models.routine_exercise import RoutineExercise
    from app.models.workout_exercise import WorkoutExercise


class Set(Base):
    __tablename__ = "sets"
    __table_args__ = (
        CheckConstraint(
            "(routine_exercise_id IS NOT NULL AND workout_exercise_id IS NULL) OR "
            "(routine_exercise_id IS NULL AND workout_exercise_id IS NOT NULL)",
            name="ck_sets_exactly_one_parent",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid4
    )
    workout_exercise_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("workout_exercises.id"), nullable=True
    )
    routine_exercise_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("routine_exercises.id"), nullable=True
    )
    order: Mapped[int] = mapped_column(nullable=False)
    set_type: Mapped[SetType] = mapped_column(
        SqlEnum(SetType, native_enum=False, length=20),
        default=SetType.NORMAL,
        nullable=False,
    )
    reps: Mapped[int | None] = mapped_column(nullable=True)
    weight: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    rpe: Mapped[Decimal | None] = mapped_column(Numeric(3, 1), nullable=True)
    completed: Mapped[bool] = mapped_column(default=False, nullable=False)

    routine_exercise: Mapped[RoutineExercise | None] = relationship(
        back_populates="sets"
    )
    workout_exercise: Mapped[WorkoutExercise | None] = relationship(
        back_populates="sets"
    )
