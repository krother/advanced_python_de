
from fixtures import galaxy


def test_pandalor(galaxy):
    assert "Pandalor" in galaxy

def test_todesstern(galaxy):
    print("tam tam tam tadada dadada")
    assert "Todesstern" not in galaxy
