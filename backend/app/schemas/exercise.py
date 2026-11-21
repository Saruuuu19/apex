from typing import Annotated, TypedDict
from uuid import UUID

from pydantic import (
    AfterValidator,
    AnyUrl,
    BaseModel,
    ConfigDict,
    Field,
    UrlConstraints,
    field_validator,
    model_validator,
    with_config,
)

from app.models.enums import Equipment, ExerciseType, MuscleGroup
from app.schemas.types import NameStr

MAX_SECONDARY_MUSCLES = len(MuscleGroup)
MAX_MEDIA_URL_LENGTH = 255


def _validate_media_url_length(url: AnyUrl) -> AnyUrl:
    if len(str(url)) > MAX_MEDIA_URL_LENGTH:
        raise ValueError(
            f"Normalized media URL must not exceed {MAX_MEDIA_URL_LENGTH} characters."
        )
    return url


HttpUrl = Annotated[
    AnyUrl,
    UrlConstraints(max_length=MAX_MEDIA_URL_LENGTH, allowed_schemes=["http", "https"]),
    AfterValidator(_validate_media_url_length),
]

class ExerciseCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: NameStr
    exercise_type: ExerciseType
    primary_muscle: MuscleGroup
    secondary_muscles: list[MuscleGroup] = Field(
        default_factory=list,
        max_length=MAX_SECONDARY_MUSCLES
    )
    equipment : Equipment
    media_url: HttpUrl | None = None

    @model_validator(mode="after")
    def validate_muscles(self) -> ExerciseCreate:
        if len(set(self.secondary_muscles)) != len(self.secondary_muscles):
            raise ValueError("Secondary muscles must not contain duplicates.")
        if self.primary_muscle in self.secondary_muscles:
            raise ValueError("The primary muscle cannot also be a secondary muscle.")
        return self

class ExerciseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: NameStr
    exercise_type: ExerciseType
    primary_muscle: MuscleGroup
    secondary_muscles: list[MuscleGroup] = Field(default_factory=list)
    equipment: Equipment
    media_url: HttpUrl | None = None

    @field_validator("secondary_muscles", mode="before")
    @classmethod
    def normalize_secondary_muscles(cls, value):
        return [] if value is None else value

@with_config(ConfigDict(extra="forbid"))
class ExerciseUpdate(TypedDict, total=False):
    name: NameStr
    exercise_type: ExerciseType
    primary_muscle: MuscleGroup
    secondary_muscles: list[MuscleGroup]
    equipment: Equipment
    media_url: HttpUrl | None
