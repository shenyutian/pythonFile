from typing import Any


class Emp:
    """工资类"""
    _num = 0
    _name = ''
    _department = ''
    _superior = 0
    _date = ''
    _salary = 0

    def __init__(self, num, name, department, superior, date, salary) -> None:
        self._num = num
        self._name = name
        self._superior = superior
        self._department = department
        self._date = date
        self._salary = salary

    def __str__(self) -> str:
        return str(self._num) + "\t"\
               + self._name + "\t"\
               + self._department + "\t"\
               + str(self._date)





