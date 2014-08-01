from com.homework.calculator.functions.MathFunctions import MathFunctions

__author__ = 'sborovskiy'

class MainFormEvents:

    def __init__(self, x, y, answer):
        self.x = x
        self.y = y
        self.answer = answer

    def ButtonDivisionEvent(event, self):
        event.__textFieldClear(event.answer)
        try:
            event.answer.insert(0, MathFunctions.division(int(event.x.get()) , int(event.y.get())))
        except ValueError:
            event.__nunValue(event.answer)

    def ButtonMultiplicationEvent(event, self):
        event.__textFieldClear(event.answer)
        try:
            event.answer.insert(0, MathFunctions.multiplication(int(event.x.get()) , int(event.y.get())))
        except ValueError:
            event.__nunValue(event.answer)

    def ButtonDifferenceEvent(event, self):
        event.__textFieldClear(event.answer)
        try:
            event.answer.insert(0, MathFunctions.difference(int(event.x.get()) , int(event.y.get())))
        except ValueError:
            event.__nunValue(event.answer)

    def ButtonSumEvent(event, self):
        event.__textFieldClear(event.answer)
        try:
            event.answer.insert(0, MathFunctions.sum(int(event.x.get()) , int(event.y.get())))
        except ValueError:
            event.__nunValue(event.answer)

    def __textFieldClear(self, answer):
        answer.delete(0, len(answer.get()))

    def __nunValue(self, answer):
        answer.insert(0, "NuN")