# Enhanced Word Ladder Solver

## Overview
An advanced implementation of the word ladder puzzle solver that finds the shortest path between two words by transforming one word into another. This enhanced version supports both traditional single-letter changes and variable-length word transformations (insertions/deletions).

## Features
- Finds minimum-length word ladders between any two valid English words
- Supports traditional single-letter substitutions
- Enhanced functionality for variable-length transformations:
  - Letter insertion at any position
  - Letter deletion at any position
- Uses queue of stacks algorithm for optimal solution finding
- Returns None if no valid ladder exists

## Project Structure
```
├── word_ladder_app.py     # Main application
├── word_ladder.py         # Core WordLadder class
├── stack.py              # Stack implementation
├── queue.py              # Queue implementation
├── words_alpha.txt       # Dictionary of English words
└── test_word_ladder.py   # Unit tests
```

## Algorithm
1. Uses a queue to manage potential ladder paths
2. Each path is stored as a stack of words
3. Implements breadth-first search to find shortest solution
4. Transformation rules:
   - Change any single letter
   - Insert a letter at any position
   - Delete a letter from any position

## Example Usage
```python
ladder = WordLadder()
print(ladder.find_ladder("cat", "hat"))    # cat -> hat
print(ladder.find_ladder("love", "hate"))  # love -> hove -> have -> hate
print(ladder.find_ladder("small", "tall")) # small -> stall -> tall
```

## Performance
- Time Complexity: O(26 * N * W * L), where:
  - N = word length
  - W = number of valid words
  - L = ladder length
- Space Complexity: O(26 * N * W)

## Dependencies
- Python 3.x
- words_alpha.txt dictionary file