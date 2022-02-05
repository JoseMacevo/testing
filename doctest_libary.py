"""
>>> recursive = Recursive()
>>> recursive.factorial(5)
120

>>> recursive.factorial(13)
6227020800
"""


class Recursive:
    def factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number -1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("test.txt")

