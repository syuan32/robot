import unittest
from main import Robot

class unitTest(unittest.TestCase):

    # test place function
    def test_place(self):
        # test with captial inputs
        robot = Robot('')
        robot.place('PLACE 2,1,SOUTH')

        self.assertTrue(robot.PLACED)
        self.assertEqual(2, robot.X)
        self.assertEqual(1, robot.Y)
        self.assertEqual('SOUTH', robot.F)
        
        # test with mixture of capital and lowercase inputs
        robot.place('place 2,2,south')

        self.assertTrue(robot.PLACED)
        self.assertEqual(2, robot.X)
        self.assertEqual(2, robot.Y)
        self.assertEqual('SOUTH', robot.F)
    
    # test invalid place for place command
    def test_invalid_place(self):
        # x is out of the table
        robot = Robot('')
        robot.place('PLACE 5,2,NORTH')
        self.assertFalse(robot.PLACED)
        
        robot.place('PLACE -1,2,NORTH')
        self.assertFalse(robot.PLACED)

        # y is out of the table
        robot.place('PLACE 2,7,NORTH')
        self.assertFalse(robot.PLACED)
        
        robot.place('PLACE 2,-1,NORTH')
        self.assertFalse(robot.PLACED)


        # f is not the right direction
        robot.place('PLACE 2,1,NORTHWEST')
        self.assertFalse(robot.PLACED)

    
    # test a success move
    def test_move(self):
        # place function should call before move
        robot = Robot('')
        robot.place('PLACE 1,2,EAST')
        robot.move()

        self.assertTrue(robot.PLACED)
        self.assertEqual(2, robot.X)
        self.assertEqual(2, robot.Y)
        self.assertEqual('EAST', robot.F)

        # another valid move
        robot.move()
        self.assertTrue(robot.PLACED)
        self.assertEqual(3, robot.X)
        self.assertEqual(2, robot.Y)
        self.assertEqual('EAST', robot.F)

    # test invalid move
    def test_invalid_move(self):
        # robot has not been placed
        robot = Robot('')
        robot.move()

        self.assertFalse(robot.PLACED)
        
        # robot has been placed, but the robot fall down from table after move
        # at west boundary
        robot.place('PLACE 0,3,WEST')
        robot.move()

        self.assertTrue(robot.PLACED)
        self.assertEqual(0, robot.X)
        self.assertEqual(3, robot.Y)
        self.assertEqual('WEST', robot.F)
        # at east boundary
        robot.place('PLACE 4,3,EAST')
        robot.move()

        self.assertTrue(robot.PLACED)
        self.assertEqual(4, robot.X)
        self.assertEqual(3, robot.Y)
        self.assertEqual('EAST', robot.F)
        # at north boundary
        robot.place('PLACE 4,4,NORTH')
        robot.move()

        self.assertTrue(robot.PLACED)
        self.assertEqual(4, robot.X)
        self.assertEqual(4, robot.Y)
        self.assertEqual('NORTH', robot.F)
        # at south boundary
        robot.place('PLACE 4,0,SOUTH')
        robot.move()

        self.assertTrue(robot.PLACED)
        self.assertEqual(4, robot.X)
        self.assertEqual(0, robot.Y)
        self.assertEqual('SOUTH', robot.F)

    
    # test successful turn
    def test_turn(self):
        robot = Robot('')
        # turn should only be call when robot has been placed on table
        robot.place('PLACE 1,2,EAST')
        
        robot.turn('LEFT')
        self.assertEqual('NORTH', robot.F)

        robot.turn('LEFT')
        self.assertEqual('WEST', robot.F)

        robot.turn('LEFT')
        self.assertEqual('SOUTH', robot.F)

        robot.turn('LEFT')
        self.assertEqual('EAST', robot.F)

        robot.turn('RIGHT')
        self.assertEqual('SOUTH', robot.F)

        robot.turn('RIGHT')
        self.assertEqual('WEST', robot.F)

        robot.turn('RIGHT')
        self.assertEqual('NORTH', robot.F)

        robot.turn('RIGHT')
        self.assertEqual('EAST', robot.F)

    def test_invalid_turn(self):
        robot = Robot('')
        # when robot has not been placed on table
        robot.turn('LEFT')

        self.assertFalse(robot.PLACED)
    

    # test successful report
    def test_report(self):
        robot = Robot('')
        # report should only be call when robot has been placed on table
        robot.place('PLACE 1,2,EAST')
        robot.report()

        self.assertTrue(robot.PLACED)
        self.assertEqual(1, robot.X)
        self.assertEqual(2, robot.Y)
        self.assertEqual('EAST', robot.F)

    def test_invalid_report(self):
        robot = Robot('')
        # when robot has not been placed on table
        robot.report()

        self.assertFalse(robot.PLACED)


    # test main function
    def test_main_function(self):
        # test valid command1 inputs
        robot1 = Robot('inputs/command1.txt')
        robot1.main()

        self.assertTrue(robot1.PLACED)
        self.assertEqual(0, robot1.X)
        self.assertEqual(1, robot1.Y)
        self.assertEqual('NORTH', robot1.F)

        # test valid command2 inputs
        robot2 = Robot('inputs/command2.txt')
        robot2.main()

        self.assertTrue(robot2.PLACED)
        self.assertEqual(0, robot2.X)
        self.assertEqual(0, robot2.Y)
        self.assertEqual('WEST', robot2.F)

        # test valid command3 inputs
        robot3 = Robot('inputs/command3.txt')
        robot3.main()

        self.assertTrue(robot3.PLACED)
        self.assertEqual(3, robot3.X)
        self.assertEqual(3, robot3.Y)
        self.assertEqual('NORTH', robot3.F)

        # input file starts with invalid commands
        robot4 = Robot('inputs/command4.txt')
        robot4.main()

        self.assertTrue(robot4.PLACED)
        self.assertEqual(3, robot4.X)
        self.assertEqual(3, robot4.Y)
        self.assertEqual('NORTH', robot4.F)


        # test valid input with multiple valid place command
        robot5 = Robot('inputs/command5.txt')
        robot5.main()

        self.assertTrue(robot5.PLACED)
        self.assertEqual(3, robot5.X)
        self.assertEqual(1, robot5.Y)
        self.assertEqual('WEST', robot5.F)

        # test an empty input file
        robot6 = Robot('inputs/empty.txt')
        robot6.main()

        self.assertFalse(robot6.PLACED)

        # test an not found input file
        robot7 = Robot('inputs/notfoundfile.txt')
        robot7.main()

        self.assertFalse(robot7.PLACED)
            

if __name__ == "__main__":
    # You can run this file using:  python tests.py
    unittest.main()
