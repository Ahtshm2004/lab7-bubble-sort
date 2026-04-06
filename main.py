"""
Bubble Sort Implementation
A learning exercise to understand the bubble sort algorithm.
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the bubble sort algorithm with progress visualization.
    
    Algorithm explanation:
    - The outer loop controls how many passes we make through the list
    - Each pass moves the largest unsorted element to its final position
    - The inner loop compares adjacent elements and swaps them if needed
    - Early exit: if no swaps occur in a pass, the list is already sorted
    
    Args:
        arr: A list of integers to be sorted
        
    Returns:
        The sorted list in ascending order
    """
    n = len(arr)
    
    # Outer loop: controls how many passes through the list we make
    # Each pass guarantees one more element is in its final position
    for i in range(n):
        # Track whether any swaps occurred in this pass
        # This helps us detect if the list is already sorted (early exit optimization)
        swaps_in_pass = 0
        
        # Inner loop: compare adjacent elements and swap if needed
        # We reduce the range by i each pass because the last i elements are already sorted
        # This optimization reduces unnecessary comparisons as we progress
        for j in range(0, n - i - 1):
            # Compare current element with the next element
            if arr[j] > arr[j + 1]:
                # If out of order, swap them using the swap() function
                swap(arr, j, j + 1)
                swaps_in_pass += 1
        
        # Print progress bar after each pass
        # This provides visual feedback about sorting progress
        print_progress_bar(i + 1, n, arr, swaps_in_pass)
        
        # Early exit optimization: if no swaps occurred, the list is already sorted
        # This allows best-case O(n) performance for pre-sorted lists
        if swaps_in_pass == 0:
            print(f"\n✓ List is sorted! (Completed in {i + 1} passes instead of {n})")
            break
    
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
    """
    # Create a prefix label if step description is provided
    # Using "if step" safely handles both None and empty string cases
    prefix = f"[{step}] " if step else ""
    print(f"{prefix}{arr}")


def print_progress_bar(pass_num: int, total_passes: int, arr: List[int], swaps: int) -> None:
    """
    Displays a visual progress bar showing the bubble sort progress.
    This provides educational visualization of how the algorithm progresses.
    
    Args:
        pass_num: Current pass number (1-indexed for readability)
        total_passes: Total number of passes needed (length of array)
        arr: Current state of the array being sorted
        swaps: Number of swaps that occurred in this pass
    """
    # Calculate progress as a percentage (0.0 to 1.0)
    # This determines how much of the progress bar to fill
    progress = pass_num / total_passes
    
    # Create the visual bar using filled (█) and empty (░) Unicode characters
    # bar_length determines how wide the progress bar appears in the terminal
    bar_length = 20
    filled_length = int(bar_length * progress)  # How many characters to fill
    bar = '█' * filled_length + '░' * (bar_length - filled_length)  # Build the bar
    
    # Format the output line with descriptive information:
    # - Pass number (with 2-digit padding for alignment)
    # - Visual progress bar
    # - Number of swaps in this pass
    # - Current state of the array being sorted
    print(f"Pass {pass_num:2d}/{total_passes} | {bar} | {swaps:2d} swaps | {arr}")


def main() -> None:
    """
    Main function to test the bubble sort implementation with visualization.
    Tests multiple scenarios to verify correctness and demonstrate the algorithm.
    """
    # Test case 1: Basic unsorted list
    print("=" * 70)
    print("TEST 1: Unsorted List")
    print("=" * 70)
    test1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {test1}")
    bubble_sort(test1)
    print(f"Sorted:   {test1}\n")
    
    # Test case 2: Already sorted list (demonstrates early exit optimization)
    print("=" * 70)
    print("TEST 2: Already Sorted List (Early Exit Optimization)")
    print("=" * 70)
    test2 = [1, 2, 3, 4, 5]
    print(f"Original: {test2}")
    bubble_sort(test2)
    print(f"Sorted:   {test2}\n")
    
    # Test case 3: Reverse sorted list (worst case for bubble sort)
    print("=" * 70)
    print("TEST 3: Reverse Sorted List (Worst Case)")
    print("=" * 70)
    test3 = [5, 4, 3, 2, 1]
    print(f"Original: {test3}")
    bubble_sort(test3)
    print(f"Sorted:   {test3}\n")
    
    # Test case 4: List with duplicates
    print("=" * 70)
    print("TEST 4: List with Duplicates")
    print("=" * 70)
    test4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print(f"Original: {test4}")
    bubble_sort(test4)
    print(f"Sorted:   {test4}\n")
    
    # Test case 5: Single element (edge case)
    print("=" * 70)
    print("TEST 5: Single Element (Edge Case)")
    print("=" * 70)
    test5 = [42]
    print(f"Original: {test5}")
    bubble_sort(test5)
    print(f"Sorted:   {test5}\n")


if __name__ == "__main__":
    main()