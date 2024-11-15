"""
hidden magic: "conftest.py" wird automatisch importiert von pytest
"""
from pathlib import Path

import pytest

from space_game import create_galaxy


BASE_PATH = Path(__file__).parent

TEST_GALAXY = BASE_PATH / "test_data/mini_galaxy.json"


@pytest.fixture(scope="module")
def galaxy():
    print("setup galaxy")
    yield create_galaxy(TEST_GALAXY)
    print("tear down galaxy")

    # geht auch
    # return create_galaxy(TEST_GALAXY)
