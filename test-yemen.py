import pytest
from project_test import yemen_game
def yemen_game_zero():
    #arrange:
    x: int = 0
    y: int = 0
    expected: int = 1

    # act:
    actual: int = yemen_game.equal(x, y)

    # Assert:
    assert actual == expected
