"""Netflix movies module."""

from typing import Any


# max = 2923706026
# min = 0
def get_highest_revenue(movies_data, flag: Any = None):
    """Get top rated movies."""
    revenue = []
    for data in movies_data:
        revenue.append(data["revenue"])
    return max(revenue) if flag else min(revenue)


# max = 2020-12-16
# min = 1911-10-12


def get_earliest_published_date(movies_data, flag: Any = None):
    """Get top rated movies."""
    published_date = []
    for data in movies_data:
        published_date.append(data["release_date"])
    return max(published_date) if flag else min(published_date)


def get_title_and_highest_or_lowest_revenue(movies_data, flag: Any = None):
    """Get top rated movies."""
    highest_revenue = get_highest_revenue(movies_data, flag)

    return [
        f'title: {d["title"]} - revenue: {"{:,}".format(d["revenue"])}'
        for d in movies_data
        if d["revenue"] == highest_revenue
    ][0]


def get_title_and_highest_or_lowest_revenue_and_release_data(
    movies_data, flag: Any = None
):
    """Get top rated movies."""
    highest_revenue = get_highest_revenue(movies_data, flag)

    return [
        f'title: {d["title"]} - revenue: {"{:,}".format(d["revenue"])} - release: {d["release_date"]}'
        for d in movies_data
        if d["revenue"] == highest_revenue
    ][0]
