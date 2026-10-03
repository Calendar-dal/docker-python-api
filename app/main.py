"""A small, production-shaped FastAPI service for numeric operations."""

from __future__ import annotations

import math
from statistics import fmean
from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field, field_validator


app = FastAPI(
    title="Numeric Utility API",
    description="Health, addition, and descriptive-statistics endpoints.",
    version="1.0.0",
)


FiniteNumber = Annotated[float, Field(allow_inf_nan=False)]


class StatisticsRequest(BaseModel):
    values: list[FiniteNumber] = Field(min_length=1, max_length=10_000)

    @field_validator("values")
    @classmethod
    def reject_non_finite_values(cls, values: list[float]) -> list[float]:
        if any(not math.isfinite(value) for value in values):
            raise ValueError("values must contain only finite numbers")
        return values


class StatisticsResponse(BaseModel):
    count: int
    mean: float
    min: float
    max: float


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/calculate", tags=["calculations"])
def calculate(
    a: Annotated[float, Query(allow_inf_nan=False)],
    b: Annotated[float, Query(allow_inf_nan=False)],
) -> dict[str, float]:
    return {"a": a, "b": b, "result": a + b}


@app.post("/statistics", response_model=StatisticsResponse, tags=["calculations"])
def statistics(payload: StatisticsRequest) -> StatisticsResponse:
    return StatisticsResponse(
        count=len(payload.values),
        mean=fmean(payload.values),
        min=min(payload.values),
        max=max(payload.values),
    )
