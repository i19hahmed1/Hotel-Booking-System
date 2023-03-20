from random import randrange
from time import sleep
from os import system

pinData = []
# pinData["person"] = object || name = string || pin = string

rooms = [
    {"number": 0, "passcode": None, "person": {"firstname": "Test", "surname": "Ing"}}
]
# rooms["number"] = interger
# rooms["passcode"] = interge
# rooms["person"] = object || firstname = string || surname = string


def BookRoom(firstname, surname):

    hasPin = False

    for i in pinData:
        if i["person"]["name"] == (firstname + surname):
            hasPin = True

    if hasPin == False:
        while True:
            print(
                "It seems you do not have a pin linked with your name, please enter a 4 digit number so that it becomes your pin. Thank You!"
            )
            newPin = input()

            if len(newPin) >= 5 or len(newPin) <= 3:
                print(
                    "You enterned a pin which has a lenth greater than or smaller than 4, try again"
                )

                sleep(2)

                system("cls")

            else:
                pinData.append({"person": {"name": firstname + surname, "pin": newPin}})
                print("I have set your pin to " + newPin)

                sleep(3)

                system("cls")
                break

    def filterName(arrName):
        if arrName["person"]["name"] == firstname + surname:
            return True
        else:
            return False

    pinCorrect = filter(filterName, pinData)[0]["person"]["pin"]

    while True:
      
        print('Please enter the pin for your account to book a room, to exit please type "0"')
      
        answerF1 = input()

        if answerF1 == "0":
            break

        if answerF1 != pinCorrect:
            print("Incorrect pin, try again")
            sleep(2)
            system("cls")
        else:
          
            rooms.append(
                {
                    "number": rooms[len(rooms) - 1]["number"] + 1,
                    "passcode": randrange(1000000, 9999999),
                    "person": {"firstname": firstname, "surname": surname},
                }
            )

            print(
            "I have added "
            + firstname
            + " "
            + surname
            + " to room "
            + str(rooms[len(rooms) - 1]["number"])
            + " your passcode is "
            + str(rooms[len(rooms) - 1]["passcode"])
            )
            
            break

    return True


def UnBookRoom(roomNumber, passcode):

    done = False

    for i in rooms:
        if i["number"] == roomNumber and i["passcode"] == passcode:
            print("I have removed the booking for room " + str(roomNumber))
            rooms.remove(i)
            done = True

    if done == False:
        print(
            "Either you put in an incorrect passcode or incorrect room number, either way I am not able to cancel your booking"
        )

        return done


def CheckBooking(firstname, surname):

    anyrooms = False
    bookedRooms = []

    for i in rooms:
        if i["person"]["firstname"] == firstname and i["person"]["surname"] == surname:
            anyrooms = True
            bookedRooms.append("room " + str(i["number"]))

    if anyrooms == True:
        print("You have the following rooms booked:\n" + "\n".join(bookedRooms))
    else:
        print("You have no rooms booked")

    return anyrooms


def CheckPasscodes(firstname, surname, pin):

    hasPin = False

    for i in pinData:
        if i["person"]["name"] == (firstname + surname):
            hasPin = True

    if hasPin == False:
        while True:
            print(
                "It seems you do not have a pin linked with your name, please enter a 4 digit number so that it becomes your pin. Thank You!"
            )
            newPin = input()

            if len(newPin) >= 5 or len(newPin) <= 3:
                print(
                    "You enterned a pin which has a lenth greater than or smaller than 4, try again"
                )

                sleep(2)

                system("cls")

            else:
                pinData.append({"person": {"name": firstname + surname, "pin": newPin}})
                print("I have set your pin to " + newPin)

                sleep(3)

                system("cls")
                break

    anyrooms = False
    bookedRooms = []

    for i in rooms:
        if i["person"]["firstname"] == firstname and i["person"]["surname"] == surname:
            anyrooms = True
            bookedRooms.append(
                "room " + str(i["number"]) + ", passcode: " + str(i["passcode"])
            )

    correctPin = False

    if anyrooms == True:

        for i in pinData:

            if pin == i["person"]["pin"]:
                print("You have the following rooms booked:\n" + "\n".join(bookedRooms))
                correctPin = True

    else:
        print("You have no rooms booked")

    if correctPin == False and anyrooms != False:
        print("Incorrect pin")

    return anyrooms


breakLoop = False

while True:
    print(
        "Please choose one of the following options:\n1. Book a room\n2. Cancel your booking\n3. Check your bookings\n4. See your room passcodes\n5. Stop program"
    )

    answer1 = input()

    if answer1 == "1":

        system("cls")

        print("Enter your firstname")
        answer2 = input()
        print("Enter your surname")
        answer3 = input()

        system("cls")

        BookRoom(answer2, answer3)

        sleep(4)

        system("cls")

    elif answer1 == "2":

        system("cls")

        print("Enter your room number")
        answer2 = int(input())
        print("Enter your passcode")
        answer3 = int(input())

        system("cls")

        UnBookRoom(answer2, answer3)

        sleep(6)

        system("cls")

    elif answer1 == "3":

        system("cls")

        print("Enter your firstname")
        answer2 = input()
        print("Enter your surname")
        answer3 = input()

        system("cls")

        CheckBooking(answer2, answer3)

        sleep(4)

        system("cls")

    elif answer1 == "4":

        system("cls")

        print("Enter your firstname")
        answer2 = input()
        print("Enter your surname")
        answer3 = input()
        print("Enter your pin")
        answer4 = input()

        system("cls")

        CheckPasscodes(answer2, answer3, answer4)

        sleep(4)

        system("cls")

    else:
        system("cls")
        breakLoop = True

    if breakLoop == True:
        break
