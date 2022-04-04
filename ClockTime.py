class ClockTime:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def setHours(self, hour):
        self.hour = hour

    def setMinutes(self, minute):
        self.minute = minute

    def setSeconds(self, second):
        self.second = second

    def setTime(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def showTime(self):
        return str(self.hour) + ":" + str(self.minute) + ":"+str(self.second)

hour = -1
minute = -1
second = -1

#ensures user inputs hour correctly
while hour > 24 or hour < 0:
        hour = int(input("Enter hour: "))
        if hour > 24 or hour < 0:
            print("Invalid input for number of hour")

#ensures user inputs minute correctly
while minute > 60 or minute < 0:
        minute = int(input("Enter minute: "))
        if minute > 60 or minute < 0:
            print("Invalid input for number of hour")

#ensures user inputs second correctly
while second > 60 or second < 0:
        second = int(input("Enter second: "))
        if second > 60 or second < 0:
            print("Invalid input for number of second")


objClock = ClockTime()
objClock.setTime(hour, minute, second)
print(objClock.showTime())