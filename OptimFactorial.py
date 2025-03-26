
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
