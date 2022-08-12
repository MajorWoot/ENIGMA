import pytest
from unittest import mock
from project import custom_enigma, default_enigma, get_input_int, get_input_list, get_input_str
import builtins





# custom_enigma(letter, r1, r2, r3, key, reflector, switchboard)
def test_custom_enigma():
    assert custom_enigma("Hello", 1, 2, 3, "AAA", 1, ["ab", "cd"] ) == ('Hello', ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'), ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'), ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'), 'AAA', 'EJMZALYXVBWFCRQUONTSPIKHGD', {'A': 'B', 'C': 'D'})
    assert custom_enigma("AAA", 1, 1, 1, "AAA", 1, ["ab"] ) == ('AAA', ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'), ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'), ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'), 'AAA', 'EJMZALYXVBWFCRQUONTSPIKHGD', {'A': 'B'})

def test_default_enigma():
    assert default_enigma("Hello") == "Hello"

def test_default_enigma_type():
    with pytest.raises(TypeError):
        default_enigma(12345)

def test_get_input_int():
    with mock.patch.object(builtins, 'input', lambda _: 1):
        assert get_input_int() == 1
    
def test_get_input_int():
    with mock.patch.object(builtins, 'input', lambda _: 7):
        with pytest.raises(SystemExit):
            get_input_int(condition=lambda x: x > 0 and x < 7) 

def test_get_input_list():
    with mock.patch.object(builtins, 'input', lambda _: "ab, cd"):
        assert get_input_list() == ["ab", "cd"]

def test_get_input_list_bad():
    with mock.patch.object(builtins, 'input', lambda _: "ab, c"):
        assert get_input_list() == ["ab"]


def test_get_input_str():
    with mock.patch.object(builtins, 'input', lambda _: "Hello"):
        assert get_input_str() == "Hello"