import subprocess
import os

# command to find the current battery percent
percent = 'pmset -g batt | grep -Eo "\d+%" | cut -d% -f1'

# command to see where the battery is getting power from
charge = 'pmset -g batt | grep "Battery Power"'

# specify the minimum percent that you want to get notified
min_percent = 30

# title of your reminder
title = 'Battery Reminder'

# text within your reminder
text = f'Battery has fallen below {min_percent}%, charge you battery sometime soon'

# function to see if the computer is plugged in or not
def is_charging(percent):
    charge_status = subprocess.run(percent, shell=True, universal_newlines=True, check=True, stdout = subprocess.PIPE)
    output = charge_status.stdout.split()[3]
    return output

# function to get the current percentage in int form
def get_percent(charge):
    battery_percent = subprocess.run(charge, shell=True, universal_newlines=True, check=True, stdout = subprocess.PIPE)
    int_battery = battery_percent.stdout.splitlines()[0]
    return int_battery

# function to notify you if your battery percent is lower than the min percent
def notify(title, text):
    current_perent = get_percent(percent)

    try:
        batt_status = is_charging(charge)
    except:
        pass

    try:
        if batt_status == "'Battery":
            if int(current_perent) < min_percent:
                os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(text, title))
    except UnboundLocalError:
        pass

if __name__ == '__main__':
    notify(title, text)
