"""Test cases for the netflix_movies module."""

from src.TDD.netflix_movies import get_earliest_published_date
from src.TDD.netflix_movies import get_highest_revenue
from src.TDD.netflix_movies import get_title_and_highest_or_lowest_revenue
from src.TDD.netflix_movies import (
    get_title_and_highest_or_lowest_revenue_and_release_data,
)


def test_get_lowest_revenue(data_fixture):
    """Test get_highest_revenue function."""
    result = get_highest_revenue(data_fixture, flag=True)
    assert result == 2923706026


def test_get_highest_revenue(data_fixture):
    """Test get_highest_revenue function."""
    result = get_highest_revenue(data_fixture, flag=False)
    assert result == 0


def test_get_latest_published_date(data_fixture):
    """Test get_earliest_published_date function."""
    result = get_earliest_published_date(data_fixture, flag=True)
    assert result == "2023-10-31"


def test_get_earliest_published_date(data_fixture):
    """Test get_earliest_published_date function."""
    result = get_earliest_published_date(data_fixture, flag=False)
    assert result == "1922-02-16"


def test_get_title_and_lowest_revenue(data_fixture):
    """Test get_title_and_highest_or_lowest_revenue function."""
    assert (
        get_title_and_highest_or_lowest_revenue(data_fixture)
        == "title: Spring Break Zombie Massacre - revenue: 0"
    )


def test_get_title_and_highest_revenue(data_fixture):
    """Test get_title_and_highest_or_lowest_revenue function."""
    assert (
        get_title_and_highest_or_lowest_revenue(data_fixture, 1)
        == "title: Avatar - revenue: 2,923,706,026"
    )


def test_get_title_and_lowest_revenue_and_release_date(data_fixture):
    """Test get_title_and_highest_or_lowest_revenue_and_release_data function."""
    assert (
        get_title_and_highest_or_lowest_revenue_and_release_data(data_fixture)
        == "title: Spring Break Zombie Massacre - revenue: 0 - release: 2016-07-07"
    )


def test_get_title_and_highest_revenue_and_release_date(data_fixture):
    """Test get_title_and_highest_or_lowest_revenue_and_release_data function."""
    assert (
        get_title_and_highest_or_lowest_revenue_and_release_data(data_fixture, 1)
        == "title: Avatar - revenue: 2,923,706,026 - release: 2009-12-15"
    )
