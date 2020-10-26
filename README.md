[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3489994&assignment_repo_type=AssignmentRepo)
# Exercise 4.26 Numbers from a file

Write a program that prompts the user for a filename, as well as the upper and lower bounds for the accepted range of numbers. Then the program reads the numbers contained in the file (each number is on its own line) and only accounts for the numbers which are inside the given range. Finally, the program should print the number of numbers that were inside the given range.

You can convert a string-type integer read from a file into a proper integer using the command `int()` (just as when handling input from a user).

```plaintext
File? **numbers-1.txt**
Lower bound? **15**
Upper bound? **20**
Numbers: 2
```

```plaintext

File? **numbers-1.txt**
Lower bound? **0**
Upper bound? **300**
Numbers: 4

```

**NB**! The exercise template comes with two files, `numbers-1.txt` and `numbers-2.txt` that have the following contents. Do not change the contents of these files.

#### numbers-1.txt:
```plaintext
300
9
20
15
```

#### numbers-2.txt:
```plaintext
123
-5
12
67
-300
1902
```
