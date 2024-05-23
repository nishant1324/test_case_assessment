import re
from collections import Counter


class MyCalculator:

    def add(self, numbers):
        if not numbers:
            return 0

        
        num_list = self.extract_numbers_only(numbers)

        integers = [int(num) for num in num_list if num and int(num) <= 1000]

        negatives = [str(num) for num in integers if num < 0]

        if negatives:
            raise ValueError(f"negative numbers not allowed: {', '.join(negatives)}")

        return self.get_sum(integers)

    def extract_numbers_only(self, input_string: str):
        if input_string.startswith("//"):
            delimiter, input_string = input_string[2:].split("\n", 1)
            input_string = input_string.replace(delimiter, ",")
        num_list = re.split("[,\n]", input_string)
        return num_list

    def get_sum(self, numbers):
        output = Counter(numbers)
        
        total = 0

        for num, count in output.items():
            if count >= 3:
                total += num ** 3
            else:
                total += num * count
        return total
