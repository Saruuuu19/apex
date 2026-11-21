from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field, field_validator

from app.schemas.sets import WorkoutSetCreate, WorkoutSetResponse
from app.schemas.types import OrderInt

MAX_SETS = 30


class WorkoutExerciseCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    exercise_id: UUID
    order: OrderInt
    sets: list[WorkoutSetCreate] = Field(min_length=1, max_length=MAX_SETS)

    @field_validator("sets")
    @classmethod
    def validate_set_order(cls, sets: list[WorkoutSetCreate]) -> list[WorkoutSetCreate]:
        if len({set_create.order for set_create in sets}) != len(sets):
            raise ValueError("Set order must be unique within an exercise.")
        return sets


class WorkoutExerciseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    workout_session_id: UUID
    exercise_id: UUID
    order: OrderInt = Field(validation_alias=AliasChoices("order", "position"))
    sets: list[WorkoutSetResponse]
