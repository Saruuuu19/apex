from typing import Annotated, TypedDict
from uuid import UUID

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, with_config

from app.schemas.types import NameStr, OrderInt

MAX_ROUTINE_EXERCISES = 50

class RoutineExerciseCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    exercise_id: UUID
    order: OrderInt


def _validate_exercise_order(
    exercises: list[RoutineExerciseCreate],
) -> list[RoutineExerciseCreate]:
    if len({exercise.order for exercise in exercises}) != len(exercises):
        raise ValueError("Exercise order must be unique within a routine.")
    return exercises


RoutineExerciseList = Annotated[
    list[RoutineExerciseCreate],
    Field(max_length=MAX_ROUTINE_EXERCISES),
    AfterValidator(_validate_exercise_order),
]


class RoutineCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: NameStr
    routine_exercises: RoutineExerciseList = Field(default_factory=list)


class RoutineExerciseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    exercise_id: UUID
    order: OrderInt


class RoutineResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    name: NameStr
    routine_exercises: list[RoutineExerciseResponse] = Field(default_factory=list)


@with_config(ConfigDict(extra="forbid"))
class RoutineUpdate(TypedDict, total=False):
    name: NameStr
    routine_exercises: RoutineExerciseList
