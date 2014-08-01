__author__ = 'sborovskiy'

class MathFunctions:

    def sum(x, y):
       """
       :param x:
       :param y:
       :return: возвращает сумму двух чисел
       """
       return x + y

    def multiplication(x, y):
       """
       :param x:
       :param y:
       :return: возвращает произведение двух чисел
       """
       return x * y

    def difference(x, y):
       """
       :param x:
       :param y:
       :return: возвращает разность двух чисел
       """
       return x - y

    def division(x, y):
       """
       :param x:
       :param y:
       :return: возвращает деление двух чисел
       """
       if y == 0:
        return 0
       else:
        return x / y
