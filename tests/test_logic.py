from app.logic import stable_hash

def test_stable_hash_deterministic():
    assert stable_hash("abc") == stable_hash("abc")
