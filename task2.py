import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Find all floats in text
    pattern = r'\b\d+\.\d+\b'
    for num in re.findall(pattern, text):
        yield float(num)

def sum_profit(text: str, func: Callable) -> float:
    # Sum all generated numbers
    return sum(func(text))

# Example usage
text = (
    "Дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
