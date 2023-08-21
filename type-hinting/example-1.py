from typing import List

def list_avg(sequence: List[float]) -> float:
    return sum(sequence) / len(sequence)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
average = list_avg(numbers)
print("Average:", average)