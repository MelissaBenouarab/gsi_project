from unit import Unit

from module import Module
from unit import Unit

def test_unit_average_and_credits():
    m1 = Module("AABD", "BD", coef=2, credit=4)
    m2 = Module("MTI", "Implémentation", coef=3, credit=5)
    m1.set_grade(tp=8, exam=9)
    m2.set_grade(tp=14, exam=13)
    u = Unit("UEM11", "Méthodo", [m1, m2])
    assert round(u.calculate_average(), 2) == round((8.6*2 + 13.4*3)/5, 2)
    assert u.calculate_credits() == 5  # seule MTI validée
