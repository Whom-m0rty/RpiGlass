import datetime

def get_time_string():
    now = datetime.datetime.now()
    hours = now.hour
    if len(str(hours)) == 1:
        hours = f'0{hours}'
    minutes = now.minute
    if len(str(minutes)) == 1:
        minutes = f'0{minutes}'
    seconds = now.second
    if len(str(seconds)) == 1:
        seconds = f'0{seconds}'
    return f'{hours}:{minutes}:{seconds}'
