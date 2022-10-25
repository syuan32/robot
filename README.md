# Toy Robot Code Challenge

## Overview

This console application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

The console application can read in commands from a .txt file of the following form:
1. PLACE X,Y,F
2. MOVE
3. LEFT
4. RIGHT
5. REPORT

`PLACE` will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner. It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.

`MOVE` will move the toy robot one unit forward in the direction it is currently facing.

`LEFT` and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

`REPORT` will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.

A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.

Input here is read from a txt file and the case of letters in input commands will not matter.

## Getting Started
You will need Python3 installed before running.

## Running
The default file path ('inputs/command1.txt') is stored in filepath.py in the app home directory, feel free to modify it when changing the inputs.

From the app home directory, to run the program, execute:
```
python3 main.py
```
You should see something like:
```
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
```

## Test
From the app home directory, run the `unittest` unit tests with:
```
python3 tests.py
```
You should see something likes:
```
PLACE 0,3,WEST
PLACE 4,3,EAST
PLACE 4,4,NORTH
PLACE 4,0,SOUTH
..Robot has not been placed on the table!
..PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
Robot has not been placed on the table!
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
PLACE 3,1,WEST
End of the input file! Robot has not been placed on the table yet!
Input file is not found!
.PLACE 1,2,EAST
MOVE
MOVE
.PLACE 2,1,SOUTH
place 2,2,south
.PLACE 1,2,EAST
REPORT
Output: 1,2,EAST
.PLACE 1,2,EAST
LEFT
LEFT
LEFT
LEFT
RIGHT
RIGHT
RIGHT
RIGHT
.
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```
# robot
