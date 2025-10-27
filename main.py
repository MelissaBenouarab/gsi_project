# -*- coding: utf-8 -*-
from module import Module
from unit import Unit
from semester import Semester

# ---------- DÉFINITION DES MODULES ----------
m1 = Module("RCB", "Réseaux des Couches Basses", coef=3, credit=6, hours_tp=1.5)
m2 = Module("ALGOAV", "Algorithmique Avancée", coef=2, credit=4, hours_tp=1.5)
m3 = Module("SE", "Systèmes d’Exploitation", coef=2, credit=4, hours_tp=1.5)
m4 = Module("AMSI", "Architecture Moderne des Systèmes Informatiques", coef=2, credit=4, hours_tp=1.5)
m5 = Module("AABD", "Architecture et Administration de Bases de Données", coef=2, credit=4, hours_tp=1.5)
m6 = Module("MTI", "Méthodes et Technologies de l’Implémentation", coef=3, credit=5, hours_tp=1.5)
m7 = Module("SCVV", "Systèmes, Communication et Virtualisation", coef=2, credit=2, hours_tp=1.5)
m8 = Module("CLOUD", "Cloud Computing", coef=1, credit=1, hours_tp=1.5)

# ---------- NOTES ----------
m1.set_grade(tp=14, exam=13)
m2.set_grade(tp=10, exam=9)
m3.set_grade(tp=12, exam=11)
m4.set_grade(tp=8, exam=7)
m5.set_grade(tp=15, exam=14)
m6.set_grade(tp=13, exam=12)
m7.set_grade(tp=11, exam=10)
m8.set_grade(tp=9, exam=8)

# ---------- UNITÉS ----------
u1 = Unit("UEF11", "UE AlgoAv et RSD", [m1, m2])
u2 = Unit("UEF12", "UE SE et AMSI", [m3, m4])
u3 = Unit("UEM11", "UE AABD et MTI", [m5, m6])
u4 = Unit("UED11", "UE SCVV", [m7])
u5 = Unit("UET11", "UE Cloud Computing", [m8])

# Coefficients des unités
u1.coef = 5
u2.coef = 4
u3.coef = 5
u4.coef = 2
u5.coef = 1

# ---------- SEMESTRE ----------
s1 = Semester("S1", "Semestre 1", [u1, u2, u3, u4, u5])

# ---------- AFFICHAGE DES RÉSULTATS ----------
print("===== RÉSULTATS DU SEMESTRE 1 (M1 GSI) =====")

for u in s1._units:
    print(f"\n{u.title} ({u.name})")
    print(f" → Moyenne unité : {u.calculate_average():.2f}")
    print(f" → Crédits obtenus : {u.calculate_credits()}")

print("\n----- Résumé global -----")
print(f"Moyenne du semestre {s1.name} : {s1.calculate_average():.2f}")
print(f"Crédits totaux obtenus : {s1.calculate_credits()}")
