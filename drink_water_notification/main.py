from plyer import notification

import time

if __name__ == '__main__':
    while True:

        notification.notify(
            title="Please Drink watar",
            message="About 15.5 cups (3.7 liters) of fluids a day for men About 11.5 cups (2.7 liters) of fluids a "
                    "day for women",
            app_icon="icon.ico",
            timeout=2

        )
        time.sleep(3600) # its remind every 1 hour
