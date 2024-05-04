"""Config test file for pytest."""

from typing import Any

import pandas as pd
import pytest


@pytest.fixture
def data_fixture() -> list[dict[Any, Any]]:
    """Data fixture."""
    file = "tests\\tmdb_10_movie.csv"

    # Read the CSV file
    df = pd.read_csv(file, encoding="utf-8")

    # clean the data by removing rows with missing values
    df = df.dropna()

    # sort the data by revenue in descending order
    df = df.sort_values(by="revenue", ascending=False).reset_index(drop=True)

    # save the data to a list of dictionaries
    data = df.to_dict(orient="records")

    return data
