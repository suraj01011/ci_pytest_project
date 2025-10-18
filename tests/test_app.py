import os, sys, math, pytest

# allow importing app.py from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import area

def test_area_basic():
    assert area(2) == 4
    assert area(3) == 9

# --- PASSING test for your Student ID (last two digits = 79) ---
def test_area_student_id_79():
    k = 79
    side = round(math.sqrt(k), 2)
    assert area(side) == pytest.approx(k, rel=1e-2, abs=1e-2)

# --- TEMPORARY FAILING TEST for the screenshot (Step A3) ---
def test_area_student_id_79_fail():
    k = 79
    side = round(math.sqrt(k), 2)
    # Intentionally wrong: k + 1 to force a failure
    assert area(side) == pytest.approx(k + 1, rel=1e-2, abs=1e-2)