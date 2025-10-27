import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gsi_project.semester import Semester
from gsi_project.unit import Unit
from gsi_project.module import Module

def test_semester_average_and_credits():
    m1 = Module("MTI", "Implémentation", coef=3, credit=5)
    m2 = Module("AABD", "BD", coef=2, credit=4)
    
    u1 = Unit("UEM11", "Méthodo", [m1, m2])
    u1.coef = 1 
    
    s1 = Semester("S1", "Semestre 1", [u1])
    
    m1.set_grade(tp=14, exam=13)
    m2.set_grade(tp=10, exam=9)
    
    assert s1.calculate_average() > 10
    assert s1.calculate_credits() == 30  
