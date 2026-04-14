import calendar
from datetime import datetime, date
from typing import Optional


def get_calendar_string(year: int) -> str:
    """
    Returns the calendar string for a given year.
    """
    return calendar.calendar(year)


def get_month_string(year: int, month: int) -> str:
    """
    Returns the calendar string for a given month.
    """
    return calendar.month(year, month)


def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.
    """
    return calendar.isleap(year)


def get_days_in_month(year: int, month: int) -> int:
    """
    Returns the number of days in a given month.
    """
    return calendar.monthrange(year, month)[1]


def get_weekday(year: int, month: int, day: int) -> str:
    """
    Returns the weekday name for a given date.
    """
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    return weekdays[calendar.weekday(year, month, day)]


def get_current_date() -> date:
    """
    Returns the current date.
    """
    return date.today()


def get_current_year() -> int:
    """
    Returns the current year.
    """
    return datetime.now().year


def get_current_month() -> int:
    """
    Returns the current month.
    """
    return datetime.now().month


def print_calendar_cli(year: Optional[int] = None, month: Optional[int] = None):
    """
    Print calendar to console. If year and month are provided, print monthly calendar.
    Otherwise, print yearly calendar.
    """
    if year is None:
        year = get_current_year()

    if month is None:
        print(f"Calendar for year {year}:")
        print(get_calendar_string(year))
    else:
        print(f"Calendar for {calendar.month_name[month]} {year}:")
        print(get_month_string(year, month))


def add_event_note(events: dict, year: int, month: int, day: int, note: str):
    """
    Add a note/event to a specific date.
    """
    key = (year, month, day)
    if key not in events:
        events[key] = []
    events[key].append(note)


def get_events(events: dict, year: int, month: int, day: int) -> list:
    """
    Get all events for a specific date.
    """
    key = (year, month, day)
    return events.get(key, [])


if __name__ == "__main__":
    current_year = get_current_year()
    current_month = get_current_month()
    current_day = get_current_date().day

    print("=" * 50)
    print(
        f"Today: {get_weekday(current_year, current_month, current_day)}, {current_year}-{current_month:02d}-{current_day:02d}"
    )
    print("=" * 50)

    print(f"\nCalendar for year {current_year}:")
    print(get_calendar_string(current_year))

    print(
        f"\nCalendar for current month ({calendar.month_name[current_month]} {current_year}):"
    )
    print(get_month_string(current_year, current_month))

    print(f"\nIs {current_year} a leap year? {is_leap_year(current_year)}")
    print(
        f"Days in {calendar.month_name[current_month]} {current_year}: {get_days_in_month(current_year, current_month)}"
    )
