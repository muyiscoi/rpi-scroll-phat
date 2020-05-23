#!/usr/bin/env python3
# script to display time on scroll phat

from datetime import datetime
import time
import scrollphat

def get_time():
    return(datetime.now().strftime("%H:%m"))

def update_display(text):
    scrollphat.write_string(text + " | ")
    scrollphat.scroll(delta=3)

def main():
    scrollphat.clear()
    while True:
        try:
            current_time = get_time()
            update_display(current_time)
            time.sleep(1)
            new_current_time = get_time()
            if current_time != new_current_time:
                update_display(new_current_time)
        except KeyboardInterrupt:
            scrollphat.clear()
            exit(1)

if __name__ == "__main__":
    main()
