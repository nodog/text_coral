import time
import random

COL_WIDTH = 80
FRAMES_PER_SECOND = 4.0

def build_coral_row(row_chars):
    random_index = random.randint(0, COL_WIDTH - 1)
    #print(random_index)
    row_chars[random_index] = '*'
    return ''.join(row_chars)


row_chars = ['.'] * COL_WIDTH

while True:
    coral_row = build_coral_row(row_chars)
    print(coral_row)
    time.sleep(1.0/FRAMES_PER_SECOND)

