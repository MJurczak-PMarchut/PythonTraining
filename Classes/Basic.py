"""
This file will explain basics of classes

A class is a template to create objects
e.g. imagine you have a couple of robots that each should perform the same function but have different motors and need
to be driven differently, if you create a object for each drive type you can select different drivers by changing
that instance

In this case we will create something like this

                            Parent class
                     --------------------------
                    |   AbstractMotorDriver   |
                    --------------------------
                                |
                            Inheritance
    Child class #1             /\\             child class #2
 -----------------------      /  \\    ---------------------------
|    MotorDriverBLDC   | ----      -- |    MotorDriverBrushed    |
------------------------              ---------------------------

"""


class AbstractMotorDriver:
    """
    Class that creates interface for motor drives
    """
    no_of_motors = 0

    def __init__(self, motor_side, motor_type):
        self.motor_side = motor_side
        self.motor_speed = 0
        self.motor_dir = 'stop'
        self.__motor_type = motor_type
        AbstractMotorDriver.no_of_motors += 1

    def __del__(self):
        AbstractMotorDriver.no_of_motors -= 1

    def drive_forward(self, speed: int):
        """
        Interface for drive_forward method
        """
        raise NotImplementedError

    def drive_backward(self, speed: int):
        """
        Interface for drive_backward method
        """
        raise NotImplementedError

    def stop(self):
        """
        Stop motor
        """
        print(f'{self.__motor_type} motor on {self.motor_side} side stopped from going in {self.motor_dir} direction'
              f' with speed of {self.motor_speed}')

    @staticmethod
    def get_number_of_motors():
        """
        A static method to return a number of instances of motor driver
        :return: number of instantiated child classes
        """
        return AbstractMotorDriver.no_of_motors


class MotorDriverBLDC(AbstractMotorDriver):
    """
    Class that creates interface for motor drives
    """

    def __init__(self, motor_side):
        super().__init__(motor_side, 'BLDC')

    def __del__(self):
        AbstractMotorDriver.no_of_motors -= 1

    def drive_forward(self, speed: int):
        """
        Drive forward on BLDC motor
        """
        self.motor_speed = speed
        self.motor_dir = 'forward'
        print(f'driving forward with speed = {speed} on {self.motor_side} BLDC motor')

    def drive_backward(self, speed: int):
        """
        Drive backward on BLDC motor
        """
        self.motor_speed = speed
        self.motor_dir = 'backward'
        print(f'driving backward with speed = {speed} on {self.motor_side} BLDC motor')

    def stop(self):
        """
        Stop motor
        """
        print(f'Stopping BLDC motor on {self.motor_side}')
        super().stop()


class MotorDriverBrushed(AbstractMotorDriver):
    """
    Class that creates interface for motor drives
    """

    def __init__(self, motor_side):
        super().__init__(motor_side, 'Brushed')

    def __del__(self):
        AbstractMotorDriver.no_of_motors -= 1

    def drive_forward(self, speed: int):
        """
        Drive forward on Brushed motor
        """
        self.motor_speed = speed
        self.motor_dir = 'forward'
        print(f'driving forward with speed = {speed} on {self.motor_side} Brushed motor')

    def drive_backward(self, speed: int):
        """
        Drive backward on Brushed motor
        """
        self.motor_speed = speed
        self.motor_dir = 'backward'
        print(f'driving backward with speed = {speed} on {self.motor_side} Brushed motor')

    def stop(self):
        """
        Stop motor
        """
        print(f'Stopping Brushed motor on {self.motor_side}')
        super().stop()


if __name__ == '__main__':
    left_motor = MotorDriverBrushed('left')
    right_motor = MotorDriverBLDC('right')
    print()
    left_motor.drive_forward(120)
    right_motor.drive_forward(180)
    print()
    """
    We can also put it in dict for easier access
    """
    Motors = {'Left': left_motor, 'Right': right_motor}

    Motors['Left'].stop()
    print()
    Motors['Right'].stop()

    print()

    print(f'We should have 2 motors, current number: {AbstractMotorDriver.get_number_of_motors()}')

    del right_motor

    print(f'We deleted a object we should expect number to go down, current number: '
          f'{AbstractMotorDriver.get_number_of_motors()}\n'
          f'But we did not delete all references to it!\n')

    del Motors['Right']

    print(f'Now we should have less active objects, current number: {AbstractMotorDriver.get_number_of_motors()}\n')

    del left_motor
    del Motors['Left']

    print(f'Now there should be no active objects, current number: {AbstractMotorDriver.get_number_of_motors()}\n')

    Motors = {
        'Left': MotorDriverBrushed('left'),
        'Right': MotorDriverBLDC('right')
    }

    print(f'Now there should be 2 active objects, current number: {AbstractMotorDriver.get_number_of_motors()}\n')

    print('Now deleting single instance in dict')
    del Motors['Left']
    print(f'Current number of instances: {AbstractMotorDriver.get_number_of_motors()}\n')
