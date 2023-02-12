import time
import argparse
import pygame


# Set default interval and break time
interval = 25
break_time = 5

def play_alarm(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Pomodoro Timer')
    parser.add_argument('-i', '--interval', type=int, help='Interval time in minutes')
    parser.add_argument('-b', '--break_time', type=int, help='Break time in minutes')
    parser.add_argument('-f', '--file_path', type=str, help='File path to MP3 file')

    args = parser.parse_args()
    return args.interval, args.break_time, args.file_path

def start_timer(interval, break_time, file_path):
    while True:
        # Start the interval timer
        print(f'Starting the interval timer for {interval} minutes')
        time.sleep(interval * 60)
        play_alarm(file_path)
        
        # Start the break timer
        print(f'Starting the break timer for {break_time} minutes')
        time.sleep(break_time * 60)
        play_alarm(file_path)

if __name__ == '__main__':
    interval, break_time, file_path = parse_arguments()
    if interval and break_time and file_path:
        start_timer(interval, break_time, file_path)
    else:
        start_timer(25, 5, "alarm.mp3")
