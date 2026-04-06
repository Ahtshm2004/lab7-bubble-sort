"""
Test suite for bubble sort implementation.

This module contains pytest tests to verify the correctness of the bubble sort
algorithm and its supporting functions.
"""

import pytest
from main import bubble_sort, swap, print_array


class TestSwap:
    """Tests for the swap function."""
    
    def test_swap_basic(self):
        """Test that swap correctly exchanges two elements."""
        arr = [1, 2, 3, 4, 5]
        swap(arr, 0, 4)
        assert arr == [5, 2, 3, 4, 1], "Swap should exchange elements at indices 0 and 4"
    
    def test_swap_adjacent(self):
        """Test that swap works with adjacent elements."""
        arr = [10, 20]
        swap(arr, 0, 1)
        assert arr == [20, 10], "Swap should exchange adjacent elements"


class TestBubbleSort:
    """Tests for the bubble_sort function."""
    
    def test_bubble_sort_unsorted_list(self):
        """Test bubble sort with an unsorted list of integers."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = bubble_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90], "Should sort unsorted list in ascending order"
    
    def test_bubble_sort_already_sorted(self):
        """Test bubble sort with an already sorted list."""
        arr = [1, 2, 3, 4, 5]
        result = bubble_sort(arr)
        assert result == [1, 2, 3, 4, 5], "Already sorted list should remain unchanged"
    
    def test_bubble_sort_reverse_order(self):
        """Test bubble sort with a list in reverse order."""
        arr = [5, 4, 3, 2, 1]
        result = bubble_sort(arr)
        assert result == [1, 2, 3, 4, 5], "Should sort reverse-ordered list correctly"
    
    def test_bubble_sort_duplicates(self):
        """Test bubble sort with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = bubble_sort(arr)
        assert result == [1, 1, 2, 3, 4, 5, 5, 6, 9], "Should handle duplicates correctly"
    
    def test_bubble_sort_single_element(self):
        """Test bubble sort with a single element."""
        arr = [42]
        result = bubble_sort(arr)
        assert result == [42], "Single element list should remain unchanged"
    
    def test_bubble_sort_empty_list(self):
        """Test bubble sort with an empty list."""
        arr = []
        result = bubble_sort(arr)
        assert result == [], "Empty list should return empty list"
    
    def test_bubble_sort_two_elements(self):
        """Test bubble sort with exactly two elements."""
        arr = [2, 1]
        result = bubble_sort(arr)
        assert result == [1, 2], "Should sort two-element list correctly"
    
    def test_bubble_sort_negative_numbers(self):
        """Test bubble sort with negative numbers."""
        arr = [-5, 3, -1, 0, 2, -8]
        result = bubble_sort(arr)
        assert result == [-8, -5, -1, 0, 2, 3], "Should handle negative numbers correctly"


class TestPrintArray:
    """Tests for the print_array function."""
    
    def test_print_array_without_step(self, capsys):
        """Test print_array output without step description."""
        arr = [1, 2, 3]
        print_array(arr)
        captured = capsys.readouterr()
        assert "[1, 2, 3]" in captured.out, "Should print array without prefix"
    
    def test_print_array_with_step(self, capsys):
        """Test print_array output with step description."""
        arr = [1, 2, 3]
        print_array(arr, "Test Step")
        captured = capsys.readouterr()
        assert "[Test Step]" in captured.out, "Should include step description in output"
        assert "[1, 2, 3]" in captured.out, "Should include array in output"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
