from operator import itemgetter
import pytest
def test_assert_true():
    assert True


def test_itemgetter():
    unsorted_data = [
        {'name': 3},
        {'name': 2},
        {'name': 1},
        ]
    assert sorted(unsorted_data, key=itemgetter('name')) == [
        {'name': 1},
        {'name': 2},
        {'name': 3},
    ]

def test_itemgetter_raises_error():
    unsorted_data = [
        {'name': 3},
        {'name': 2},
        {'name': 1},
        ]
    with pytest.raises(KeyError):
        sorted(unsorted_data, key=itemgetter('nme'))

def test_sort_if_different_keys_provided():
    unsorted_data = [
        {'name': 3},
        {'name': 2},
        {'name': 1},
        {'nae': 1},
        ]
    assert sorted(unsorted_data, key=itemgetter('name')) == [
        {'name': 3},
        {'name': 2},
        {'name': 1},
        {'nae': 1},
        ]
