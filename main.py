import fileinput
from filepath import file_path

class Robot:
    def __init__(self, file_path: str):
        # Initialize global Variables 
        self.X = 0
        self.Y = 0
        self.F = 'EAST'
        # robot is placed on table
        self.PLACED = False
        self.file_path = file_path

    def main(self):
        # read input from files
        try:
            for command in fileinput.input(files=self.file_path):
                # call executeCommand function 
                self.executeCommand(command)
            # if the input file does not include any valid place command
            if not self.PLACED:
                print('End of the input file! Robot has not been placed on the table yet!')
        except:
            print('Input file is not found!')
        return


    # execute each command
    def executeCommand(self, command: str):
        command = command.upper().rstrip()
        if command == 'MOVE':
            self.move()
        elif command == 'LEFT':
            self.turn(command)
        elif command == 'RIGHT':
            self.turn(command)
        elif command == 'REPORT':
            self.report()
        else:
            # call place, the command will be further validated in this function
            self.place(command)
        
    # place the robot
    def place(self, command: str):
        directions = ('EAST', 'SOUTH', 'WEST', 'NORTH')
        split_command = command.split(' ')
        # if command follow the 'PLACE X,Y,F' format, then further validate the palce command
        if split_command[0].upper() == 'PLACE':
            # get the X,Y,F if command if valid
            place_command = split_command[1].split(',')
            if len(place_command) == 3:
                nX = int(place_command[0])
                nY = int(place_command[1])
                nF = place_command[2].upper().rstrip()
                # input validation and robot location updating
                if 0 <= nX < 5 and 0 <= nY < 5 and nF in directions:
                    print(command)
                    self.X = nX
                    self.Y = nY
                    self.F = nF
                    self.PLACED = True

    # turn left & right action if robot is on the table
    def turn(self, command: str):
        # use a map (key: F, values:(left, right)) to access the right and left of each facing(F) 
        turn_direction = {'EAST': ('NORTH', 'SOUTH'), 'SOUTH': (
            'EAST', 'WEST'), 'WEST': ('SOUTH', 'NORTH'), 'NORTH': ('WEST', 'EAST')}
        if self.PLACED:
            print(command)
            if command == 'LEFT':
                self.F = turn_direction[self.F][0]
            else:
                self.F = turn_direction[self.F][1]
            
    # execuate the move action
    def move(self):
        move_forward = {'EAST': (1, 0), 'SOUTH': (
            0, -1), 'WEST': (-1, 0), 'NORTH': (0, 1)}
        d = move_forward[self.F]
        # if the location after moving is valid then update location
        if self.PLACED and 0 <= (self.X + d[0]) < 5 and 0 <= (self.Y + d[1]) < 5:
            print('MOVE')
            self.X = self.X + d[0]
            self.Y = self.Y + d[1]

    # report current robot location if applicable
    def report(self):
        # report current location only when robot is on the table
        if self.PLACED:
            print('REPORT')
            print(f'Output: {self.X},{self.Y},{self.F}')
        else:
            # set a reminder to place the robot on table first
            print('Robot has not been placed on the table!')
        
if __name__ == '__main__':
    # You can run this file using:  python main.py
    robot = Robot(file_path)
    robot.main()
