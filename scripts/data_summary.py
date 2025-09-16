# data_summary.py
"""
A simple script to demonstrate basic data operations
"""
import numpy as np

def main():
    # Sample earnings data (in thousands)
    earnings_data = [45, 52, 38, 67, 43, 55, 49, 61, 39, 58]

    # Your task: Calculate these statistics without using any libraries
    # Think about how you would compute each of these manually

    mean_earnings = sum(earnings_data) / len(earnings_data)
    median_earnings = sorted(earnings_data)[len(earnings_data) // 2] if len(earnings_data) % 2 != 0 else \
        (sorted(earnings_data)[len(earnings_data) // 2 - 1] + sorted(earnings_data)[len(earnings_data) // 2]) / 2
    max_earnings = max(earnings_data)
    min_earnings = min(earnings_data)

    print(f"Earnings Analysis:")
    print(f"Mean: ${mean_earnings:.2f}k")
    print(f"Median: ${median_earnings:.2f}k") 
    print(f"Range: ${min_earnings:.2f}k - ${max_earnings:.2f}k")

if __name__ == "__main__":
    main()