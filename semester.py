from academicelement import AcademicElement

class Semester(AcademicElement):
    """Représente un semestre académique contenant plusieurs unités."""

    def __init__(self, name, title, units=None):
        super().__init__(name, title)
        self._units = units if units is not None else []

    def add_unit(self, unit):
        self._units.append(unit)

    def calculate_average(self):
        """Calcule la moyenne du semestre à partir des unités."""
        if not self._units:
            return 0
        total = sum(u.calculate_average() * u.coef for u in self._units)
        coef_sum = sum(u.coef for u in self._units)
        return total / coef_sum if coef_sum != 0 else 0

    def calculate_credits(self):
        """Calcule le total des crédits validés du semestre."""
        if not self._units:
            return 0

        avg = self.calculate_average()

        # ✅ Si la moyenne du semestre >= 10, tous les crédits (30) sont obtenus
        if avg >= 10:
            return 30

        # ❌ Sinon, calcul détaillé par unités
        total_credits = sum(u.calculate_credits() for u in self._units)
        return total_credits
