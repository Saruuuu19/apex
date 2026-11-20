from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.schemas.types import OrderInt


class RoutineExerciseCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    exercise_id: UUID
    order: OrderInt


class RoutineExerciseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    exercise_id: UUID
    order: OrderInt
