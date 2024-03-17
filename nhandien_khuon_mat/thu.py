from datetime import datetime,date
import datetime

Gio = datetime.datetime.now().strftime("%H")
Phut = datetime.datetime.now().strftime("%M")
Giay = datetime.datetime.now().strftime("%S")

robot_brain = Gio + " Giờ " + Phut + " Phút " + Giay + " Giây"

print(robot_brain)