from email import message
from operator import truediv
from socket import timeout
import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please Stand Up and Walk!!",
            message = "To reduce the risk of a bad posture please stand up and walk around!",
            timeout=20

        )
        time.sleep(60*30)

        notification.notify(
            title = "Please Drink Water",
            message = "Staying hydrated is essential to a healthy lifestyle",
            timeout=20

        )
        time.sleep(60*30)

        
