# Bubble Sort Implementation

A learning-focused implementation of the **bubble sort algorithm** in Python, designed to understand sorting mechanisms, algorithm analysis, and test-driven development.

## 📚 Overview

This project provides a clean, well-documented implementation of the bubble sort algorithm with comprehensive test coverage. It's ideal for students learning:
- How sorting algorithms work
- Python fundamentals (loops, functions, type hints)
- Software testing with pytest
- Git version control workflows
- Defensive programming practices

## 🎯 What is Bubble Sort?

Bubble sort is a simple sorting algorithm that:
1. **Repeatedly compares** adjacent elements in a list
2. **Swaps them** if they're in the wrong order
3. **Continues** until the entire list is sorted

### Time Complexity
- **Best Case:** O(n) — when list is already sorted
- **Average Case:** O(n²)
- **Worst Case:** O(n²) — when list is in reverse order

### Space Complexity
- O(1) — sorts in-place with no extra space needed

## 📁 Project Structure

```
lab7-bubble-sort/
├── main.py              # Core implementation
├── test_main.py         # Comprehensive test suite
├── README.md            # This file
├── REPORT.md            # Project report
├── JOURNAL.md           # Interaction log
└── .github/
    ├── copilot-instructions.md
    └── agents/
        └── journal-logger.agent.md
```

## 🔧 Installation

### Prerequisites
- Python 3.7+
- pytest (for running tests)

### Setup

1. Clone or navigate to the repository:
```bash
cd lab7-bubble-sort
```

2. Install testing dependencies:
```bash
pip install pytest
```

## 💻 Usage

### Run the Application

Execute the main program with test cases:
```bash
python main.py
```

**Expected Output:**
```
--- Testing: Unsorted ---
Original: [64, 34, 25, 12, 22, 11, 90]
Result:   [11, 12, 22, 25, 34, 64, 90]

--- Testing: Already Sorted ---
Original: [1, 2, 3, 4, 5]
Result:   [1, 2, 3, 4, 5]

--- Testing: Empty List ---
Original: []
Result:   []

--- Testing: Single Element ---
Original: [42]
Result:   [42]
```

### Run Tests

Execute the comprehensive test suite:
```bash
python -m pytest test_main.py -v
```

Run with coverage report:
```bash
python -m pytest test_main.py -v --cov=main
```

## 📖 API Reference

### `bubble_sort(arr: List[int]) -> List[int]`

Sorts a list of integers using the bubble sort algorithm.

**Parameters:**
- `arr` (List[int]): A list of integers to be sorted

**Returns:**
- List[int]: The sorted list in ascending order

**Example:**
```python
from main import bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

### `swap(arr: List[int], i: int, j: int) -> None`

Swaps two elements at specified indices in a list.

**Parameters:**
- `arr` (List[int]): The list containing elements to swap
- `i` (int): Index of the first element
- `j` (int): Index of the second element

**Example:**
```python
from main import swap

arr = [1, 2, 3, 4, 5]
swap(arr, 0, 4)
print(arr)  # Output: [5, 2, 3, 4, 1]
```

### `print_array(arr: List[int], step: str = "") -> None`

Prints the current state of an array with optional step description.

**Parameters:**
- `arr` (List[int]): The list to print
- `step` (str, optional): Description of the current step (default: "")

**Example:**
```python
from main import print_array

arr = [5, 2, 8, 1, 9]
print_array(arr)                           # Output: [5, 2, 8, 1, 9]
print_array(arr, "After first pass")       # Output: [After first pass] [5, 2, 8, 1, 9]
```

## ✅ Test Coverage

The project includes **12 comprehensive tests** organized in 3 test classes:

### TestSwap (2 tests)
- Basic element swapping
- Adjacent element swapping

### TestBubbleSort (8 tests)
- Unsorted list sorting
- Already sorted lists
- Reverse-ordered lists
- Lists with duplicate elements
- Single element lists
- Empty lists
- Two-element lists
- Lists with negative numbers

### TestPrintArray (2 tests)
- Output without step description
- Output with step description

**Test Results:**
```
12 passed in 0.04s ✅
```

Run all tests:
```bash
python -m pytest test_main.py -v
```

## 🚀 Key Features

✅ **Clean, Readable Code**
- Type hints for all functions
- Comprehensive docstrings
- PEP 8 compliant

✅ **Educational Value**
- Step-by-step comments explaining algorithm logic
- TODO markers guide learning process
- Handles edge cases gracefully

✅ **Robust Testing**
- 12 unit tests covering core functionality
- Edge case validation
- Output verification

✅ **Version Control**
- Git repository with meaningful commits
- Complete interaction journal in JOURNAL.md
- Traceable development history

## 🔍 How Bubble Sort Works (Step by Step)

Given list: `[5, 2, 8, 1, 9]`

### Pass 1:
```
[5, 2, 8, 1, 9]  → Compare 5 and 2, swap
[2, 5, 8, 1, 9]  → Compare 5 and 8, no swap
[2, 5, 8, 1, 9]  → Compare 8 and 1, swap
[2, 5, 1, 8, 9]  → Compare 8 and 9, no swap
[2, 5, 1, 8, 9]  → Largest element (9) is now in correct position
```

### Pass 2:
```
[2, 5, 1, 8, 9]  → Continue comparing and swapping...
[2, 1, 5, 8, 9]
```

### Pass 3:
```
[1, 2, 5, 8, 9]  → Final sorted array
```

## 💡 Learning Outcomes

After completing this project, you should understand:

1. **Algorithm Fundamentals**
   - How bubble sort compares and swaps elements
   - Why time complexity matters
   - Trade-offs between simplicity and efficiency

2. **Python Programming**
   - Using loops for iteration
   - Function parameters and return types
   - Type hints for code clarity
   - Tuple unpacking for efficient swaps

3. **Software Development Practices**
   - Writing testable code
   - Test-driven development (TDD)
   - Using pytest framework
   - Git workflows and version control

4. **Problem-Solving**
   - Breaking complex problems into smaller functions
   - Thinking about edge cases
   - Defensive programming

## 🔮 Future Enhancements

Potential improvements to explore:

- [ ] Add a `debug` parameter to `bubble_sort()` for optional verbose output
- [ ] Implement early-exit optimization (stop if no swaps occur in a pass)
- [ ] Add performance benchmarking
- [ ] Compare bubble sort with other algorithms (quick sort, merge sort)
- [ ] Add visualization of sorting steps
- [ ] Implement command-line argument parsing

## 📝 Notes

- This implementation sorts in **ascending order**
- The algorithm sorts **in-place** (modifies the original list)
- Suitable for **educational purposes** — not recommended for production use on large datasets

## 🤝 Contributing

This is an educational project. Feel free to:
- Extend the implementation with optimizations
- Add more test cases
- Experiment with variants of bubble sort
- Create performance visualizations

## 📄 License

Educational project for learning purposes.

---

**Created:** April 2026  
**Language:** Python 3.7+  
**Framework:** pytest for testing  
**Version Control:** Git
