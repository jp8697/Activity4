import pytest
from polygon import Polygon
#Step 1
def test_init():
    polygon1 = Polygon("Square", [3.5, 3.5, 3.5, 3.5])
    assert polygon1.name == "Square"
    assert polygon1.sides == [3.5, 3.5, 3.5, 3.5]

def test_getpolygon():
    polygon1 = Polygon("Square", [3.5, 3.5, 3.5, 3.5])
    assert polygon1.get_name() == "Square"
    assert polygon1.get_sides() == [3.5, 3.5, 3.5, 3.5]

def test_setpolygon():
    polygon1 = Polygon("Square", [3.5, 3.5, 3.5, 3.5])
    polygon1.set_name("Rectangle")
    polygon1.set_sides([4.5, 4.5, 4.5, 4.5])
    assert polygon1.get_name() == "Rectangle"
    assert polygon1.get_sides() == [4.5, 4.5, 4.5, 4.5]

#Step 2
def test_equality():
    polygon1 = Polygon("Square", [3.5, 3.5, 3.5, 3.5])
    polygon2 = Polygon("Square", [3.5, 3.5, 3.5, 3.5])
    assert polygon1 == polygon2

def test_inequality():
    polygon1 = Polygon("Square", [3.5, 3.5, 3.5, 3.5])
    polygon2 = Polygon("Rectangle", [4.0, 4.0, 4.0, 4.0])
    assert polygon1 != polygon2

#Step 3
def test_polygon_str():
    polygon1 = Polygon("Rectangle", [4.0, 4.0, 4.5, 4.5])
    output = "Rectangle has sidelenghts of [4.0, 4.0, 4.5, 4.5]"
    assert str(polygon1) == output

#Step 4
def test_circumference():
    polygon1 = Polygon("Rectangle", [4.0, 4.0, 4.5, 4.5])
    assert polygon1.circumference() == pytest.approx(17)
