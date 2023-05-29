import time

TIME_IN_MINUTES = 5
TOTAL_TIME_IN_SECONDS = TIME_IN_MINUTES * 60

def show_break_message(*, seconds=TOTAL_TIME_IN_SECONDS):
    while seconds > 0:
        time.sleep(1)
        seconds = seconds - 1
        print(f'Starting stream in {seconds} seconds')
    
show_break_message(seconds=10*60)