from academicelement import AcademicElement

class Unit(AcademicElement):

    def __init__(self, name, title, modules=None):
        super().__init__(name, title)
        self._modules = modules if modules is not None else []

    def add_module(self, module):
        self._modules.append(module)

    def calculate_average(self):
        if not self._modules:
            return 0
        total = sum(m.calculate_average() * m.coef for m in self._modules)
        coef_sum = sum(m.coef for m in self._modules)
        return total / coef_sum if coef_sum != 0 else 0

    def calculate_credits(self):
        if not self._modules:
            return 0

        avg = self.calculate_average()
        if avg >= 10:
            total_credits = sum(m.credit for m in self._modules)
        else:
            total_credits = sum(m.calculate_credits() for m in self._modules)

        return total_credits

if __name__ == "__main__":
    from module import Module

    m1 = Module("MTI", "Methods & Technologies of Implementation", coef=3, credit=5, hours_tp=1.5)
    m2 = Module("AABD", "Database Architecture and Administration", coef=2, credit=4, hours_tp=1.5)

    m1.set_grade(tp=14, exam=12)
    m2.set_grade(tp=8, exam=6)

    u1 = Unit("UEM11", "UE Méthodologie", [m1, m2])

    print(f"Moyenne {m1.name}: {m1.calculate_average():.2f}")
    print(f"Moyenne {m2.name}: {m2.calculate_average():.2f}")
    print(f"Moyenne unité {u1.name}: {u1.calculate_average():.2f}")
    print(f"Crédits unité: {u1.calculate_credits()}")
