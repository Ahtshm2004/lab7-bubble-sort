"""
Bubble Sort Implementation
A learning exercise to understand the bubble sort algorithm.
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the bubble sort algorithm.
    
    Args:
        arr: A list of integers to be sorted
        
    Returns:
        The sorted list in ascending order
        
    TODO: Implement the outer loop that controls how many passes through the list
    TODO: Implement the inner loop that compares adjacent elements
    TODO: Implement the swap logic when elements are out of order
    """
    # TODO: Start your implementation here
    n = len(arr)
    # The outer loop ensures we pass through the list enough times
    for i in range(n):
        # The inner loop compares adjacent elements
        # We use n - i - 1 because the last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap logic when elements are out of order
                swap(arr, j, j + 1)
                print_array(arr, f"Swapped indices {j} and {j+1}")
                
    return arr


def swap(arr: List[int], i: int, j: int) -> None:
    """
    Swaps two elements at indices i and j in the list.
    
    Args:
        arr: The list containing the elements to swap
        i: Index of the first element
        j: Index of the second element
        
    TODO: Implement the swap logic (hint: you can use tuple unpacking in Python)
    """
    # TODO: Start your implementation here
    arr[i], arr[j] = arr[j], arr[i]


def print_array(arr: List[int], step: str = "") -> None:
    """
    Prints the current state of the array for visualization/debugging.
    
    Args:
        arr: The list to print
        step: Optional description of what step this represents
        
    TODO: Implement to print the array nicely (consider using f-strings)
    """
    # TODO: Start your implementation here
    prefix = f"[{step}] " if step else ""
    print(f"{prefix}{arr}")


def main() -> None:
    """
    Main function to test the bubble sort implementation.
    
    TODO: Create a test list with unsorted integers
    TODO: Call bubble_sort() with your test list
    TODO: Print the original and sorted arrays
    TODO: Consider testing edge cases (empty list, single element, already sorted)
    """
    # TODO: Start your implementation here
    test_cases = {
        "Unsorted": [64, 34, 25, 12, 22, 11, 90],
        "Already Sorted": [1, 2, 3, 4, 5],
        "Empty List": [],
        "Single Element": [42]
    }

    for name, data in test_cases.items():
        # Work on a copy to keep the original for comparison
        original = list(data)
        print(f"\n--- Testing: {name} ---")
        print(f"Original: {original}")
        
        sorted_arr = bubble_sort(data)
        
        print(f"Result:   {sorted_arr}")


if __name__ == "__main__":
    main()