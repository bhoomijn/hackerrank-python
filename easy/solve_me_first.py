"""
Problem: Solve Me First
Difficulty: Easy
Link: https://www.hackerrank.com/challenges/solve-me-first

Description:
    Complete the function that adds two integers and returns their sum.

Time Complexity: O(1)
Space Complexity: O(1)

Approach: Simple arithmetic operation
"""

def solveMeFirst(a, b):
    """
    Add two integers and return their sum.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: Sum of a and b
    """
    return a + b


# Test Cases
if __name__ == "__main__":
    print(solveMeFirst(2, 3))  # Output: 5
    print(solveMeFirst(-5, 10))  # Output: 5
    print(solveMeFirst(0, 0))  # Output: 0
