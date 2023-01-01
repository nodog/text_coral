from math import sin
import random

class _Urchin:
    position = -1
    symbol = '*'

    def __init__(self, position):
        self.position = position
    

class _Fan:
    position = -1
    symbol = '|'
    phase_across_row = 0.0
    amplitude = 15.0
    period_in_sec = 3.0
    frames_per_second = 1.0
    PI = 3.141592653589

    def __init__(self, position, global_variables):
        self.position = position
        self.frames_per_second = global_variables["frames_per_second"]

    def get_position(self, frame_count):
        phi = 0
        t = frame_count / self.frames_per_second
        x = self.amplitude * sin(2.0 * self.PI * t / self.period_in_sec + phi) + self.position
        return int(x)




class CoralMode:
    global_variables = {}
    col_width = 0
    coral_row = ['.']
    n_urchins = 0
    n_fans =  0
    urchins = []
    fans = []

    def __init__(self, global_variables):
        self.global_variables = global_variables
        self.col_width = self.global_variables["col_width"]

        self.coral_row = ['.'] * self.col_width
        self.n_urchins = random.randint(0, self.col_width//15) + 1
        self.n_fans =  random.randint(0, self.col_width//10) + 1

        for i in range(self.n_urchins):
            self.urchins.append(_Urchin(random.randint(0,self.col_width) - 1))
        for i in range(self.n_fans):
            self.fans.append(_Fan(random.randint(0,self.col_width) - 1, self.global_variables))
            
        return
    
    def get_next_row(self, frame_count):
        self.coral_row = ['.'] * self.col_width

        for i in range(self.n_urchins):
            self.coral_row[self.urchins[i].position] = self.urchins[i].symbol
            # print(self.urchins[i].position)

        for i in range(self.n_fans):
            x = self.fans[i].get_position(frame_count)
            if ( 0 < x ) and (x < self.col_width):
                self.coral_row[x] = self.fans[i].symbol
            # print(self.fans[i].position)

        return  ''.join(self.coral_row)