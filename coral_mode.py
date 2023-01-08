from math import sin
import random

class _Urchin:
    position = -1
    symbol = '*'

    def __init__(self, position):
        self.position = position
    

class _Fan:
    position = -1
    symbol = '8'
    PI = 3.141592653589
    phase_across_row = 2.0 * PI / 2.0
    MAX_PHASE_VARIATION = 2.0 * PI / 2.0
    phase_variation = 0.0
    amplitude = 9.0
    period_in_sec = 3.0
    frames_per_second = 1.0
    col_width = 80

    def __init__(self, position, symbol, global_variables):
        self.position = position
        self.symbol = symbol
        self.frames_per_second = global_variables["frames_per_second"]
        self.col_width = global_variables["col_width"]
        self.phase_variation = self.MAX_PHASE_VARIATION * random.random()

    def get_position(self, frame_count):
        phi = self.phase_across_row * self.position / self.col_width + self.phase_variation
        t = frame_count / self.frames_per_second
        x = self.amplitude * sin(2.0 * self.PI * t / self.period_in_sec + phi) + self.position
        return int(x)


class CoralMode:
    global_variables = {}
    col_width = 0
    coral_row = [' ']
    chars_by_brightness = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    n_urchins = 0
    n_fans =  0
    urchins = []
    fans = []

    def __init__(self, global_variables):
        self.global_variables = global_variables
        self.col_width = self.global_variables["col_width"]

        self.coral_row = self._create_coral_row(self.col_width)
        self.n_urchins = random.randint(2, self.col_width//15) + 1
        self.n_fans =  random.randint(2, self.col_width//3) + 1

        for i in range(self.n_urchins):
            self.urchins.append(_Urchin(random.randint(0,self.col_width) - 1))
        for i in range(self.n_fans):
            self.fans.append(_Fan(random.randint(0,self.col_width) - 1, 
            self.chars_by_brightness[73 + random.randint(-5,5)], 
            self.global_variables))
            
        return
    
    def _create_coral_row(self, col_width):
        coral_row = []
        brightness_char = random.randint(0,10)
        for i in range(col_width):
            coral_row.append(self.chars_by_brightness[brightness_char])
            new_brightness_char = brightness_char + random.randint(-1,1)

            if (0 <= new_brightness_char and new_brightness_char < len(self.chars_by_brightness)):
                brightness_char = new_brightness_char

        return coral_row

    def get_next_row(self, frame_count):
        new_coral_row = self.coral_row.copy()

        for i in range(self.n_urchins):
            new_coral_row[self.urchins[i].position] = self.urchins[i].symbol
            # print(self.urchins[i].position)

        for i in range(self.n_fans):
            x = self.fans[i].get_position(frame_count)
            if ( 0 < x ) and (x < self.col_width):
                new_coral_row[x] = self.fans[i].symbol
            # print(self.fans[i].position)

        return  ''.join(new_coral_row)