import pytest
from app.logic import stable_hash


def test_stable_hash_deterministic():
    assert stable_hash("abc") == stable_hash("abc")


def test_stable_hash_range():
    result = stable_hash("any-string")
    assert 0 <= result < 100


def test_stable_hash_empty_string():
    assert stable_hash("") == 0


def test_stable_hash_unicode():
    result = stable_hash("üsküdar")
    assert isinstance(result, int)


def test_stable_hash_invalid_type():
    with pytest.raises(TypeError):
        stable_hash(123)
