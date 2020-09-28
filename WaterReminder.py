import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = " *** Reminder For Drinking Water *** ",
            message = " Your daily water level not reached please drink water now",
            app_icon = r"C:\Users\Chakraborty PC\Desktop\rupy\water.ico",
            timeout = 15
        )
        time.sleep(60*15)
