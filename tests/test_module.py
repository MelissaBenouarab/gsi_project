from module import Module

from module import Module

def test_module_average():
    m = Module("MTI", "Méthodes et Technologies de l’Implémentation", coef=3, credit=5, hours_tp=1.5)
    m.set_grade(tp=14, exam=12)
    assert round(m.calculate_average(), 2) == 12.8  # attendu

def test_module_credit():
    m = Module("MTI", "Méthodes et Technologies de l’Implémentation", coef=3, credit=5)
    m.set_grade(tp=14, exam=12)
    assert m.calculate_credits() == 5  # moyenne > 10 donc crédit validé
