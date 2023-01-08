import os
import time
import coral_mode

size = os.get_terminal_size();

frame_count = 0

global_variables = {
    "col_width": size.columns,
    "frames_per_second": 20.0,
}

mode = coral_mode.CoralMode(global_variables)

while True:
    coral_row = mode.get_next_row(frame_count)
    print(coral_row)
    frame_count += 1
    time.sleep(1.0/global_variables["frames_per_second"])

