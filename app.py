command=""
started=False
stopped=False
while True:
    command = input("<").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started=True
            stopped=False
            print("Car started! Ready to Go")
    elif command=="stop":
        if stopped:
            print("Car already stooped")
        else:
            stopped=True
            started=False
            print("Car stopped! relax")
    elif command == "help":
        print("""
Stop: Stop the car
Start : start the car
Quit : exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand")

