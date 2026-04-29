# Sudoku (Easy Level) Solver using CSP

**Author:** Dharun Venkat

## Problem Description
Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9. This project implements an easy-level Sudoku solver using the Constraint Satisfaction Problem (CSP) paradigm.

## Algorithms Used
The problem is modeled as a Constraint Satisfaction Problem (CSP). The primary algorithm used is **Backtracking Search**:
- **Variables**: The empty cells in the 9x9 grid.
- **Domains**: The numbers 1 through 9.
- **Constraints**: 
  - A number can appear only once in a given row.
  - A number can appear only once in a given column.
  - A number can appear only once in a given 3x3 subgrid.
The algorithm assigns a valid value from the domain to an empty cell and recursively attempts to solve the rest of the board. If a conflict occurs, it backtracks and tries the next valid value.

## Execution Steps

### Python (Command Line)
1. Ensure you have Python installed on your system (Python 3.x recommended).
2. Clone this repository or download the source code.
3. Navigate to the `Sudoku_CSP_Solver` directory.
4. Run the Python script using the following command:
   ```bash
   python sudoku_csp.py
   ```
5. The program will output the solved Sudoku grid to the console.

### Interactive Website
You can view and test the interactive Sudoku solver by opening the `index.html` file in any web browser. 
Alternatively, use this raw.githack link to view the interactive website live:
[Interactive Sudoku Solver](https://raw.githack.com/dharunv2k7-sys/AI_ProblemSolving_-RA2411026050105-/main/Sudoku_CSP_Solver/index.html)

## Sample Output
```
Sudoku solved successfully:
3 1 6 5 7 8 4 9 2 
5 2 9 1 3 4 7 6 8 
4 8 7 6 2 9 5 3 1 
2 6 3 4 1 5 9 8 7 
9 7 4 8 6 3 1 2 5 
8 5 1 7 9 2 6 4 3 
1 3 8 9 4 7 2 5 6 
6 9 2 3 5 1 8 7 4 
7 4 5 2 8 6 3 1 9 
```
