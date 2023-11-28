import statistics

class StatsCalculator:
    def calculate(self, name: str, x: list[float]) -> float:
        if name == "average":
            return self.average(x)
        elif name == "variance":
            return statistics.variance(x)
        elif name == "standard dev":
            return statistics.stdev(x)
        elif name == "median":
            return statistics.median(x)
        else:
            print("Function not found!")
            return -1

    def average(self, x: list[float]) -> float:
        """Calculate the average of a list of numbers."""
        return sum(x) / len(x) if x else 0

# Usage
calculator = StatsCalculator()
data = [1, 2, 3, 4, 5]
print(calculator.calculate("average", data))
print(calculator.calculate("variance", data))
print(calculator.calculate("standard dev", data))
print(calculator.calculate("median", data))
