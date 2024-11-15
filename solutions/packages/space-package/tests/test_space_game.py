from fixtures import galaxy
from space_game import SpaceGame
from space_game import cli
from functools import partial
from unittest import mock, TestCase
from unittest.mock import MagicMock


def test_pandalor(galaxy):
    assert "Pandalor" in galaxy


def test_todesstern(galaxy):
    print("tam tam tam tadada dadada")
    assert "Todesstern" not in galaxy


def test_repr(galaxy):
    assert repr(galaxy["Pandalor"]).startswith("<Pandalor")


def dummy_input(gen) -> str:
    return next(gen)


class TestCli(TestCase):

    def setUp(self):
        gen = (x for x in "1231x")
        self.dummy_func = partial(dummy_input, gen=gen)

    def test_cli(self):   # <-- capsys: builtin fixture catpuring stdout
        """Wir ersetzen die Tastatureingabe durch eine künstliche Dummy-Funktion == Mocking"""
        with mock.patch.object(SpaceGame, "get_command", self.dummy_func):  # avoids side effect on other tests
            SpaceGame.main()
        
        #output = capsys.readouterr().out  # FIXME: verhielt sich komisch, nämlich gar nicht
        
    def test_get_command(self):
        m = MagicMock()
        with mock.patch.object(cli, "input", m):
            SpaceGame.get_command()
        assert m.call_count == 1

    def tearDown(self):
        print("tear down test data")
