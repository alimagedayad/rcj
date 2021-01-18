# import RPi.GPIO as io

class l289n():
    """A class to control one side of an L298N dual H bridge motor driver."""

    def __init__(self, in1, in2, in3, in4, testing=0):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.testing = testing
        if self.testing == 1:
            print(f"{'='*10} Testing mode {'='*10}")
            print("Pin 1: %1d, Pin 2: %1d, Pin 3: %1d, Pin 4: %1d" %(self.in1, self.in2, self.in3, self.in4))
        all_pins = [self.in1, self.in2, self.in3, self.in4]
        # io.setmode(io.BCM)
        # io.setup(all_pins, io.OUT)
        # io.setwarnings(False)

    def forwards(self):
        if self.testing == 1:
            print('Moving forward!')
            return ''
        else:
            pass
            # io.output(self.in1, 1)
            # io.output(self.in2, 0)
            # io.output(self.in3, 1)
            # io.output(self.in4, 0)

    def backwards(self):
        if self.testing == 1:
            print('Moving backward!')
            return 0
        else:
            pass
            # io.output(self.in1, 0)
            # io.output(self.in2, 1)
            # io.output(self.in3, 0)
            # io.output(self.in4, 1)

    def left(self):
        if self.testing == 1:
            print('Turning left!')
            return ''
        else:
            pass
            # io.output(self.in1, 0)
            # io.output(self.in2, 1)
            # io.output(self.in3, 1)
            # io.output(self.in4, 0)

    def right(self):
        if self.testing == 1:
            print('Turning right!')
            return ''
        else:
            # io.output(self.in1, 1)
            # io.output(self.in2, 0)
            # io.output(self.in3, 0)
            # io.output(self.in4, 1)
            pass

    def uturn(self):
        if self.testing == 1:
            print('U-turning!')
            return ''
        else:
            pass
            # io.output(self.in1, 1)
            # io.output(self.in2, 1)
            # io.output(self.in3, 1)
            # io.output(self.in4, 1)

    def stop(self):
        if self.testing == 1:
            print('Moving forward!')
            return ''
        else:
            pass
            # io.output(self.in1, 0)
            # io.output(self.in2, 0)
            # io.output(self.in3, 0)
            # io.output(self.in4, 0)

    def cleanup(self):
        pass
        # io.cleanup()
        # io.setmode(io.BCM)
