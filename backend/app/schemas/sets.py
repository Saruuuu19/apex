from typing import TypedDict
from uuid import UUID

from pydantic import BaseModel, ConfigDict, with_config

from app.models.enums import SetType
from app.schemas.types import OrderInt, RepsInt, RpeDecimal, WeightDecimal


class _SetFields(BaseModel):
    order: OrderInt
    set_type: SetType = SetType.NORMAL
    reps: RepsInt | None = None
    weight: WeightDecimal | None = None
    rpe: RpeDecimal | None = None


class RoutineSetCreate(_SetFields):
    model_config = ConfigDict(extra="forbid")


class RoutineSetResponse(_SetFields):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


@with_config(ConfigDict(extra="forbid"))
class RoutineSetUpdate(TypedDict, total=False):
    reps: RepsInt | None
    weight: WeightDecimal | None
    rpe: RpeDecimal | None


class WorkoutSetCreate(_SetFields):
    model_config = ConfigDict(extra="forbid")

    completed: bool = False


class WorkoutSetResponse(_SetFields):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    completed: bool


@with_config(ConfigDict(extra="forbid"))
class WorkoutSetUpdate(TypedDict, total=False):
    reps: RepsInt | None
    weight: WeightDecimal | None
    rpe: RpeDecimal | None
    completed: bool
