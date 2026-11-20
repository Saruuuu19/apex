from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator, Field, StringConstraints


def normalize_username(username: str) -> str:
    return username.strip().lower()


NameStr = Annotated[str, Field(max_length=100)]
UsernameStr = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True, max_length=50, pattern=r"^[A-Za-z0-9_]+$"
    ),
    AfterValidator(normalize_username),
]
WeightDecimal = Annotated[Decimal, Field(max_digits=6, decimal_places=2)]
RpeDecimal = Annotated[Decimal, Field(max_digits=3, decimal_places=1)]
RepsInt = int
OrderInt = int
