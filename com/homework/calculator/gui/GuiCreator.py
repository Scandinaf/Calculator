import tkinter
from com.homework.calculator.events.MainFormEvents import MainFormEvents

__author__ = 'sborovskiy'


class GuiCreator:

    WINDOW_SIZE = "200x200"
    FONT_SIZE = "Arial 13"
    PADDING = 17

    def _createGui(self, name):
        self.__createMainWindow(name)
        self.valueX = self.__createTextField("Введите значение x")
        self.valueY = self.__createTextField("Введите значение y")
        self.answer = self.__createTextField("Ответ")
        mainFormEvents = MainFormEvents(self.valueX, self.valueY, self.answer)
        self.__createButton("+", mainFormEvents.ButtonSumEvent)
        self.__createButton("-", mainFormEvents.ButtonDifferenceEvent)
        self.__createButton("*", mainFormEvents.ButtonMultiplicationEvent)
        self.__createButton("/", mainFormEvents.ButtonDivisionEvent)
        self.__interfaceRun()

    def __createMainWindow(self, name):
        root = tkinter.Tk()
        root.title(name)
        root.geometry(GuiCreator.WINDOW_SIZE)
        root.resizable(0,0)
        self.root = root

    def __createTextField(self, text):
        self.__createLabel(text)
        textField = tkinter.Entry(self.root)
        textField.pack()
        return textField

    def __createLabel(self, text):
        tkinter.Label(self.root, text=text, font=GuiCreator.FONT_SIZE).pack()

    def __createButton(self, text, event):
        button = tkinter.Button(self.root)
        button['text'] = text
        button.bind("<Button-1>", event)
        button.pack(side = tkinter.LEFT, padx = GuiCreator.PADDING)

    def __interfaceRun(self):
        self.root.mainloop()


