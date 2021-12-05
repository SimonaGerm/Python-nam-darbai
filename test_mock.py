import datetime


def is_weekday():
    today = datetime.datetime.today()
    # monday = 0, sunday = 6
    return 0 <= today.weekday() < 5


if __name__ == '__main__':
    from unittest.mock import Mock

    # save a couple of test days
    tuesday = datetime.datetime(year=2021, month=11, day=30)
    saturday = datetime.datetime(year=2021, month=12, day=4)

    datetime = Mock()
    datetime.datetime.today.return_value = saturday
    assert not is_weekday()