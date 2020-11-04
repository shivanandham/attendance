import pyautogui 
import time 
import sms


def detect(num, api):
    while 1:
        if pyautogui.locateOnScreen('glogo.png', confidence=0.6) != None:
            print("Detected attendance link")
            sms.send(num, api)
            exit_code = input('\n1.Run again\n2.Exit\n')
            if exit_code == '2':
                print('See you again')
                exit(0)
            if exit_code == '1':
                print("\nOpen your class meeting's message box in teams and relax")
                detect(num, api)
        else:
            time.sleep(1)


def start():
    num, api = get_data()
    action = input('''Welcome to attendance notifier.
Enter the number to perform coresponding action.
1.Start detection
2.Change mobile number and api key
''')
    
    if action == '1':
        print("\nOpen your class meeting's message box in teams and relax")
        detect(num, api)
    if action == '2':
        w_data()
        start()

def is_data():
    read_data = open("data.txt", 'r')
    data = read_data.readlines()
    return len(data)
def get_data():
    read_data = open("data.txt", 'r')
    data = read_data.readlines()
    num = data[0].rstrip()
    api = data[1].rstrip()
    return num, api
def w_data():
    write_data = open('data.txt', 'w')
    data = []
    print()
    num = input("Enter your phone number: ")+'\n'
    api = input("Enter your fast2sms api key: ")
    data.append(num)
    data.append(api)
    write_data.writelines(data)
    print('Data successfully saved\n')



if is_data()==0:
    print('First time setup')
    w_data()
    start()
else:
    start()