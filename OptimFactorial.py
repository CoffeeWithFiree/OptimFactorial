import math
class OptimFactorial:
    @staticmethod
    def NaivAlgorithm(n):
        """Naive algorithm, not the most optimal.
        Just multiply all the numbers from 1 to n"""
        try:
            fact = 1
            for i in range(2, n + 1):
                fact = fact * i
            return fact
        except:
            raise Exception("incorrect input")

    @staticmethod
    def TreeAlgorithm(n):
        """"""
        if n >= 2:
            return OptimFactorial.RekursTree(2, n)
        elif n >= 0:
            return 1
        else:
            return 0

    @staticmethod
    def RekursTree(a, b):
        if b - a == 1:
            return b * a
        elif a == b:
            return a
        else:
            midd = math.floor((b + a) / 2)
            return OptimFactorial.RekursTree(a, midd) * OptimFactorial.RekursTree(midd + 1, b)
