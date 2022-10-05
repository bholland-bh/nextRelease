from freezegun import freeze_time

from main import next_release


@freeze_time("01/10/2022")
def test_2201_a():
    assert next_release() == '2201-a'


@freeze_time("01/24/2022")
def test_2201_b():
    assert next_release() == '2201-b'


@freeze_time("02/07/2022")
def test_2202_a():
    assert next_release() == '2202-a'


@freeze_time("02/21/2022")
def test_2202_b():
    assert next_release() == '2202-b'


@freeze_time("03/07/2022")
def test_2203_a():
    assert next_release() == '2203-a'


@freeze_time("03/21/2022")
def test_2203_b():
    assert next_release() == '2203-b'


@freeze_time("03/21/2022")
def test_2203_b():
    assert next_release() == '2203-b'


@freeze_time("04/04/2022")
def test_2204_a():
    assert next_release() == '2204-a'


@freeze_time("04/18/2022")
def test_2204_b():
    assert next_release() == '2204-b'


@freeze_time("05/02/2022")
def test_2205_a():
    assert next_release() == '2205-a'


@freeze_time("05/16/2022")
def test_2205_b():
    assert next_release() == '2205-b'


@freeze_time("05/30/2022")
def test_2206_a():
    assert next_release() == '2206-a'


@freeze_time("06/13/2022")
def test_2206_a():
    assert next_release() == '2206-b'


@freeze_time("06/27/2022")
def test_2206_a():
    assert next_release() == '2206-c'


@freeze_time("07/11/2022")
def test_2206_a():
    assert next_release() == '2207-a'


@freeze_time("07/25/2022")
def test_2206_a():
    assert next_release() == '2207-b'


@freeze_time("08/08/2022")
def test_2206_a():
    assert next_release() == '2208-a'


@freeze_time("08/22/2022")
def test_2206_a():
    assert next_release() == '2208-b'


@freeze_time("09/05/2022")
def test_2206_a():
    assert next_release() == '2209-a'


@freeze_time("09/19/2022")
def test_2206_a():
    assert next_release() == '2209-b'


@freeze_time("10/03/2022")
def test_2206_a():
    assert next_release() == '2210-a'


@freeze_time("10/17/2022")
def test_2206_a():
    assert next_release() == '2210-b'


@freeze_time("10/31/2022")
def test_2206_a():
    assert next_release() == '2211-a'


@freeze_time("11/14/2022")
def test_2206_a():
    assert next_release() == '2211-b'


@freeze_time("11/28/2022")
def test_2206_a():
    assert next_release() == '2211-c'


@freeze_time("12/12/2022")
def test_2206_a():
    assert next_release() == '2212-a'


@freeze_time("12/26/2022")
def test_2206_a():
    assert next_release() == '2212-b'
