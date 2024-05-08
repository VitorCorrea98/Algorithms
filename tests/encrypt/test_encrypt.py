from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("fluzao", 5) == "azulf_o"
    assert encrypt_message("fluzao", 2) == "oazu_lf"
    assert encrypt_message("fluzao", 10) == "oazulf"
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 3) == "ulf_oaz"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("fluzao", "flu") == "ulf_oaz"
