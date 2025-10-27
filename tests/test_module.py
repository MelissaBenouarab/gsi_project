import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from module import Module

def test_calculate_average():
    m = Module("MTI", "Méthodes et Technologies de l’Implémentation", coef=3, credit=5)
    m.set_grade(tp=14, exam=12)
    assert round(m.calculate_average(), 2) == 12.4
