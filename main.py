from calendar import Calendar, WEDNESDAY, SUNDAY
from datetime import datetime, timedelta


def next_release() -> str:
    today = datetime.today().date()

    # first release date of 2022
    release_date = datetime.strptime('01/12/22', '%m/%d/%y').date()

    release_dates = [release_date]
    date = release_date
    while date.year == today.year:
        # next release is _almost_ always 2 weeks from previous release
        date += timedelta(days=14)
        release_dates.append(date)

    # determine the date of the next release by
    next_release_date = None
    for release_date in release_dates:
        if release_date > today:
            next_release_date = release_date
            break

    weds_dates = []
    # gets list of wednesdays in current month
    for week in Calendar(firstweekday=SUNDAY).monthdatescalendar(today.year, today.month):
        for day in week:
            if day.weekday() == WEDNESDAY and day.month == today.month:
                weds_dates.append(day)

    release_suffix = ""
    # determine which wednesday of the month that falls on
    for idx, weds in enumerate(weds_dates):
        if weds == next_release_date:
            if idx <= 1:
                # first or second wednesday
                release_suffix = "a"
            elif idx < 5:
                release_suffix = "b"
            else:
                release_suffix = "c"
            break

        # need to handle case where next release is on a holiday and pick the wednesday after

    year = str(today.year)[2:]
    month = '{d.month:02}'.format(d=today)

    return year + month + "-" + release_suffix


if __name__ == "__main__":
    next_release()
