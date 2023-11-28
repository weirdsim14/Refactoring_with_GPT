import statistics

class StatsCalculator:
    @staticmethod
    def average(x: list[float]) -> float:
        """Calculate the average of a list of numbers."""
        return sum(x) / len(x) if x else 0

    @staticmethod
    def variance(x: list[float]) -> float:
        """Calculate the variance of a list of numbers."""
        return statistics.variance(x)

    @staticmethod
    def standard_deviation(x: list[float]) -> float:
        """Calculate the standard deviation of a list of numbers."""
        return statistics.stdev(x)

    @staticmethod
    def median(x: list[float]) -> float:
        """Calculate the median of a list of numbers."""
        return statistics.median(x)

# Usage
data = [1, 2, 3, 4, 5]
print(StatsCalculator.average(data))
print(StatsCalculator.variance(data))
print(StatsCalculator.standard_deviation(data))
print(StatsCalculator.median(data))
