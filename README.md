# sudokuPy
Python version of Sudoku Solver developed by Lee Hsien Loong
Original C++ Script: [Google Drive](http://bit.ly/1zfIGMc)
## How to use
1. Download the python script and run
```bash
python sudoku.py
```
2. Enter all 9 rows of the Sudoku inputs one by one. For example:
```bash
Row[1] : ---------
Row[2] : -----3-85
Row[3] : --1-2----
Row[4] : ---5-7---
Row[5] : --4---1--
Row[6] : -9-------
Row[7] : 5------73
Row[8] : --2-1----
Row[9] : ----4---9
```
## developing steps
1. Use ChatGPT 3.5
[ChatGPT](https://chatgpt.com/?oai-dm=1)
Prompt: `Help me convert this C++ code into Python code:`
```c++
// Paste the original C++ code from Sudoku2.cpp here
```
2. Debug the Error
Python Error Message:
```bash
$ python ~/Downloads/Sudoku/sudoku.py
Row[1] : ---------
Row[2] : -----3-85
Row[3] : --1-2----   
Row[4] : ---5-7---
Row[5] : --4---1--
Row[6] : -9-------
Row[7] : 5------73
Row[8] : --2-1----
Row[9] : ----4---9
Traceback (most recent call last):
  File "~/Downloads/Sudoku/sudoku.py", line 171, in <module>
    main()
  File "~/Downloads/Sudoku/sudoku.py", line 166, in main
    place(SeqPtr)
  File "~/Downloads/Sudoku/sudoku.py", line 143, in place
    place(S + 1)
  File "~/Downloads/Sudoku/sudoku.py", line 143, in place
    place(S + 1)
  File "~/Downloads/Sudoku/sudoku.py", line 143, in place
    place(S + 1)
  [Previous line repeated 61 more times]
  File "~/Downloads/Sudoku/sudoku.py", line 119, in place
    LevelCount[S] += 1
IndexError: list index out of range
```
The bug from original code by ChatGPT:
```python
def place(S):
  LevelCount[S] += 1
  globals()['Count'] += 1
  
  S2 = next_seq(S)
  swap_seq_entries(S, S2)
  
  if S >= 81:
    succeed()
    return
```

Debug: in the function `def place(S);`, move the `if S >= 81:` ahead:
```python
def place(S):
# move the if ahead
  if S >= 81:
    succeed()
    return
  LevelCount[S] += 1
  globals()['Count'] += 1

  S2 = next_seq(S)
  swap_seq_entries(S, S2)
```

3. Test Code
```bash
$ python ~/Downloads/Sudoku/soduku.py
Row[1] : ---------
Row[2] : -----3-85
Row[3] : --1-2----
Row[4] : ---5-7---
Row[5] : --4---1--
Row[6] : -9-------
Row[7] : 5------73
Row[8] : --2-1----
Row[9] : ----4---9

 987 654 321
 246 173 985
 351 928 746

 128 537 694
 634 892 157
 795 461 832

 519 286 473
 472 319 568
 863 745 219

Level Counts:

(3, 9):   1 (8, 9):   2 (4, 9):   4 (5, 9):   8 (6, 9):  15 (1, 9):  23 
(3, 8):  33 (8, 8):  46 (4, 8):  79 (1, 8): 119 (5, 8): 182 
(6, 8): 250 (9, 8): 287 (4, 7): 347 (6, 7): 478 (6, 5): 588 
(6, 1): 732 (6, 3): 828 (6, 4): 862 (6, 6): 895 (4, 5): 795 
(4, 3): 761 (5, 5): 843 (7, 5): 829 (2, 5): 616 (1, 5): 594 
(2, 7): 543 (2, 3): 565 (7, 3): 551 (2, 4): 577 (3, 6): 565 
(3, 4): 590 (1, 4): 572 (1, 6): 595 (7, 4): 612 (5, 4): 576 
(7, 6): 476 (7, 7): 389 (7, 2): 262 (4, 2): 184 (2, 2): 140 
(2, 1):  95 (5, 6):  56 (8, 7):  34 (8, 6):  18 (3, 1):  13 
(8, 1):  10 (3, 7):   7 (3, 2):   8 (1, 7):  10 (5, 1):  10 
(5, 2):   6 (8, 2):   4 (8, 4):   2 (9, 1):   1 (1, 1):   1 
(9, 2):   1 (9, 3):   1 (9, 4):   1 (4, 1):   1 (9, 6):   1 
(9, 7):   1 (1, 3):   1 (1, 2):   1 

Count = 17697


Total Count = 24394
```

