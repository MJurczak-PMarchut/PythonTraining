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

    def get_number_of_motors(self):
        return AbstractMotorDriver.no_of_motors


class MotorDriverBLDC(AbstractMotorDriver):
    """
    Class that creates interface for motor drives
    """

    def __init__(self, motor_side):
        super().__init__(motor_side, 'BLDC')
        AbstractMotorDriver.no_of_motors += 1

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
        AbstractMotorDriver.no_of_motors += 1

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

    left_motor.drive_forward(120)
    right_motor.drive_forward(180)

    """
    We can also put it in dict for easier access
    """
    Motors = {'Left': left_motor, 'Right': right_motor}

    Motors['Left'].stop()
    Motors['Right'].stop()

    print(AbstractMotorDriver(None, None).get_number_of_motors())
