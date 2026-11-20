from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.sets import RoutineSetCreate, RoutineSetResponse
from app.schemas.types import OrderInt


class RoutineExerciseCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    exercise_id: UUID
    order: OrderInt
    sets: list[RoutineSetCreate] = Field(min_length=1)


class RoutineExerciseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    exercise_id: UUID
    order: OrderInt
    sets: list[RoutineSetResponse]
