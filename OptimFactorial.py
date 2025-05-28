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
        """The optimal algorithm is a recursive algorithm based on the idea
        that the multipliers are always approximately the same length."""
        if n >= 2:
            return OptimFactorial.RekursTree(2, n)
        elif n >= 0:
            return 1
        else:
            return 0

    @staticmethod
    def RekursTree(a, b):
        """recursive division of multipliers into pairs"""
        if b - a == 1:
            return b * a
        elif a == b:
            return a
        else:
            midd = math.floor((b + a) / 2)
            return OptimFactorial.RekursTree(a, midd) * OptimFactorial.RekursTree(midd + 1, b)

    @staticmethod
    def FactFactor(n):
        """Calculation algorithm by factorization"""
        simple_nums = OptimFactorial.SieveofEratosthenes(n)
        degrees_ = []
        for cur_num in simple_nums:
            i = cur_num
            sum_ = 0
            while i <= n:
                sum_ += int(n / i)
                i *= cur_num
            degrees_.append(sum_)
        result = 1
        for k in range(len(simple_nums)):
            result *= pow(simple_nums[k], degrees_[k])
        return result


    @staticmethod
    def SieveofEratosthenes(n):
        """the algorithm for finding prime numbers"""
        nums = [i for i in range(2, n + 1)]
        mask = [1 for _ in range(2, n + 1)]
        step = 2
        while step * step < n:
            index_num = nums.index(step)
            index_start = nums.index(step * step)
            for i in range(index_start, len(nums), step):
                mask[i] = 0
            for j in range(index_num + 1, len(nums)):
                if mask[j] == 1:
                    step = nums[j]
                    break
        simple_nums = []
        for i in range(len(nums)):
            if mask[i] == 1:
                simple_nums.append(nums[i])

        return simple_nums