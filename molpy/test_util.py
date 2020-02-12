import pytest
import molpy
@pytest.mark.parametrize("point1, point2 , bench", [
    ([0,1], [0,0], 1), 
    ([0,2], [0,0], 2)
    ])
def test_distance(point1, point2, bench):
    assert molpy.program.distance(point1, point2) ==bench
