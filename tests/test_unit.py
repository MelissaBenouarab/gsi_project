import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gsi_project.unit import Unit
from gsi_project.module import Module

def test_unit_average():
    m1 = Module("AABD", "Base de données", coef=2, credit=4)
    m1.set_grade(tp=10, exam=12)
    u = Unit("UEM11", "Méthodologie", [m1])
    assert round(u.calculate_average(), 2) == 11.2
