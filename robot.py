import wpilib
from wpilib.drive import MecanumDrive
from wpilib.interfaces import GenericHID
Hand = GenericHID.Hand

class MyRobot(wpilib.SampleRobot):
    # Channels on the roboRIO that the motor controllers are plugged in to
    frontLeftChannel = 0
    rearLeftChannel = 2
    frontRightChannel = 1
    rearRightChannel = 3

    # The channel on the driver station that the joystick is connected to
    joystickChannel = 0

    def robotInit(self):
        """Robot initialization function"""
        self.frontLeftMotor = wpilib.Talon(self.frontLeftChannel)
        self.rearLeftMotor = wpilib.Talon(self.rearLeftChannel)
        self.frontRightMotor = wpilib.Talon(self.frontRightChannel)
        self.rearRightMotor = wpilib.Talon(self.rearRightChannel)

        # invert the left side motors
        self.frontLeftMotor.setInverted(True)

        # you may need to change or remove this to match your robot
        self.rearLeftMotor.setInverted(True)

        self.drive = MecanumDrive(
            self.frontLeftMotor,
            self.rearLeftMotor,
            self.frontRightMotor,
            self.rearRightMotor,
        )

        self.drive.setExpiration(0.1)

        self.stick = wpilib.XboxController(self.joystickChannel)
        self.speed = 0.5

    def operatorControl(self):
        """Runs the motors with Mecanum drive."""

        self.drive.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():
            # Use the joystick X axis for lateral movement, Y axis for forward movement, and Z axis for rotation.
            # This sample does not use field-oriented drive, so the gyro input is set to zero.
            self.drive.driveCartesian(
                (self.speed*self.stick.getX()), (self.speed*self.stick.getY()), (self.speed*self.stick.getX(Hand.kLeft))
            )

            wpilib.Timer.delay(0.005)  # wait 5ms to avoid hogging CPU cycles


if __name__ == "__main__":
    wpilib.run(MyRobot)
