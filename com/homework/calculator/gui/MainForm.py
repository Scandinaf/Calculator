from com.homework.calculator.gui.GuiCreator import GuiCreator

__author__ = 'sborovskiy'

class MainForm:

    def __init__(self,name = "Calculator"):
        self.name = name
        self.__createMainForm(name)


    def __createMainForm(self, name):
        GuiCreator()._createGui(name)

