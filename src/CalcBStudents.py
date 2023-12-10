# -*- coding: utf-8 -*-
from Types import DataType


class CalcBStudents:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        b_students_count = 0
        for key in self.data:
            only_b_marks = True
            for subject in self.data[key]:
                if subject[1] < 75:
                    only_b_marks = False
                    break
            if only_b_marks:
                b_students_count += 1
        return b_students_count
