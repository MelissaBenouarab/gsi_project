from academicelement import AcademicElement

class Module(AcademicElement):

    def __init__(
        self,
        name: str = "",
        title: str = "",
        coef: int = 1,
        credit: int = 1,
        hours_lecture: float = 1.5,
        hours_td: float = 0,
        hours_tp: float = 0,
        teaching_mode: str = "In-person",
        continous_percent: int = 40,
        exam_percent: int = 60
    ):
        super().__init__(name, title)
        self.coef = coef
        self.credit = credit
        self.hours_lecture = hours_lecture
        self.hours_td = hours_td
        self.hours_tp = hours_tp
        self.teaching_mode = teaching_mode
        self.evaluation_continous_percent = continous_percent
        self.evaluation_exam_percent = exam_percent
        self._grades = {"tp": 0, "td": 0, "exam": 0}

    def set_grade(self, tp=None, td=None, exam=None):
        if tp is not None:
            self._grades["tp"] = tp
        if td is not None:
            self._grades["td"] = td
        if exam is not None:
            self._grades["exam"] = exam

    def calculate_average(self):
        tp = self._grades.get("tp", 0)
        exam = self._grades.get("exam", 0)
        return (tp * 0.4) + (exam * 0.6)

    def calculate_credits(self):
        avg = self.calculate_average()
        return self.credit if avg >= 10 else 0
