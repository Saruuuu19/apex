from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import JSON, String, Uuid
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import Equipment, ExerciseType, MuscleGroup

if TYPE_CHECKING:
    from app.models.routine_exercise import RoutineExercise
    from app.models.workout_exercise import WorkoutExercise


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid4
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    exercise_type: Mapped[ExerciseType] = mapped_column(
        SqlEnum(ExerciseType, native_enum=False, length=20), nullable=False
    )
    # Change to ´MuscleGroup | None´ if decide to put CARDIO EXERCISES AS NON MUSCLE EXERCISES
    primary_muscle: Mapped[MuscleGroup] = mapped_column(
        SqlEnum(MuscleGroup, native_enum=False)
    )
    secondary_muscles: Mapped[list[MuscleGroup] | None] = mapped_column(
        JSON, nullable=True
    )
    equipment: Mapped[Equipment] = mapped_column(
        SqlEnum(Equipment, native_enum=False, length=10), nullable=False
    )
    media_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    routine_exercises: Mapped[list[RoutineExercise]] = relationship(
        back_populates="exercise"
    )
    workout_exercises: Mapped[list[WorkoutExercise]] = relationship(
        back_populates="exercise"
    )
