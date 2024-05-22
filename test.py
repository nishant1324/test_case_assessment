import re


class MyCalculator:

    def add(self, numbers):
        if not numbers:
            return 0

        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)
            numbers = numbers.replace(delimiter, ",")
        num_list = re.split("[,\n]", numbers)

        integers = [int(num) for num in num_list if num and int(num) <= 1000]

        negatives = [str(num) for num in integers if num < 0]

        if negatives:
            raise ValueError(f"negative numbers not allowed: {', '.join(negatives)}")

        return sum(integers)
