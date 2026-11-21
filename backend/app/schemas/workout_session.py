from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.schemas.types import NameStr
from app.schemas.workout_exercise import WorkoutExerciseCreate, WorkoutExerciseResponse

MAX_WORKOUT_EXERCISES = 50

class WorkoutSessionCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    routine_id: UUID | None = None
    workout_exercises: list[WorkoutExerciseCreate] = Field(
        min_length=1, max_length=MAX_WORKOUT_EXERCISES
    )

    @field_validator("workout_exercises")
    @classmethod
    def validate_exercise_order(
        cls, exercises: list[WorkoutExerciseCreate]
    ) -> list[WorkoutExerciseCreate]:
        if len ({exercise.order for exercise in exercises}) != len(exercises):
            raise ValueError("Exercise order must be unique within a workout session.")
        return exercises

class WorkoutSessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    routine_id: UUID | None = None
    routine_name: NameStr | None = None
    started_at: datetime
    completed_at: datetime | None = None
    workout_exercises: list[WorkoutExerciseResponse]

class WorkoutSessionUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    completed_at: datetime | None = None
