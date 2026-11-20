from typing import TypedDict
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, with_config

from app.schemas.routine_exercise import RoutineExerciseCreate, RoutineExerciseResponse
from app.schemas.types import NameStr

MAX_ROUTINE_EXERCISES = 50


class RoutineCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: NameStr
    routine_exercises: list[RoutineExerciseCreate] = Field(
        min_length=1, max_length=MAX_ROUTINE_EXERCISES
    )

    @field_validator("routine_exercises")
    @classmethod
    def validate_exercise_order(
        cls, exercises: list[RoutineExerciseCreate]
    ) -> list[RoutineExerciseCreate]:
        if len({exercise.order for exercise in exercises}) != len(exercises):
            raise ValueError("Exercise order must be unique within a routine.")
        return exercises


class RoutineResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    name: NameStr
    routine_exercises: list[RoutineExerciseResponse]


@with_config(ConfigDict(extra="forbid"))
class RoutineUpdate(TypedDict, total=False):
    name: NameStr
