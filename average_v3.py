class AverageCalculator:
    def __init__(self):
        self.numbers = []

    def get_numbers(self):
        for i in range(5):
            x = float(input("enter a number"))
            self.numbers.append(x)

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

    def __str__(self):
        return f"The average is: {self.calculate_average()}"


calc = AverageCalculator()
calc.get_numbers()
print(calc.calculate_average())
print(calc)
