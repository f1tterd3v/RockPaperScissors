import time

def compare(move, rps):
    if (move == 1 and rps == 1):
        print("Double rock! it's a draw, please go again")
        time.sleep(0.5)
    elif(move == 1 and rps == 2):
        print("Paper beats rock! you lost that time, try again")
        time.sleep(0.5)

    elif(move == 1 and rps == 3):
        print("Rock smashes scissors! you win! please select again")
        time.sleep(0.5)
    elif (move == 2 and rps == 1):
        print("Paper beats rock! You win! please select again")
        time.sleep(0.5)
    elif (move == 2 and rps == 2):
        print("Double paper! it's a draw, please go again")
        time.sleep(0.5)
    elif (move == 2 and rps == 3):
        print("scissors cut paper! you lost that time, try again")
        time.sleep(0.5)
    elif (move == 3 and rps == 1):
        print("Rock smashes scissors! you lost that time, please select again")
        time.sleep(0.5)
    elif (move == 3 and rps == 2):
        print("scissors cut paper! you win!, please go again")
        time.sleep(0.5)
    else:
        print("double scissors! that's a draw, please go again again")
        time.sleep(0.5)