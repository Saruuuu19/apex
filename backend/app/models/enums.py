from enum import StrEnum


class ExerciseType(StrEnum):
    CARDIO = "CARDIO"
    STRENGTH = "STRENGTH"


class Equipment(StrEnum):
    NONE = "NONE"
    DUMBBELL = "DUMBBELL"
    BARBELL = "BARBELL"
    KETTLEBELL = "KETTLEBELL"
    MACHINE = "MACHINE"


class MuscleGroup(StrEnum):
    CHEST = "CHEST"
    LATS = "LATS"
    UPPER_BACK = "UPPER_BACK"

    REAR_DELTS = "REAR_DELTS"
    SIDE_DELTS = "SIDE_DELTS"
    FRONT_DELTS = "FRONT_DELTS"

    BICEPS = "BICEPS"
    TRICEPS = "TRICEPS"
    FOREARMS = "FOREARMS"

    ABS = "ABS"
    LOWER_BACK = "LOWER_BACK"

    QUADS = "QUADS"
    HAMSTRINGS = "HAMSTRINGS"
    GLUTES = "GLUTES"
    CALVES = "CALVES"
    ADDUCTORS = "ADDUCTORS"
    ABDUCTORS = "ABDUCTORS"


class SetType(StrEnum):
    WARM_UP = "WARM_UP"
    DROP_SET = "DROP_SET"
    NORMAL = "NORMAL"
    FAILURE = "FAILURE"
