def click():
    time.sleep(float(user_input2))
    pyautogui.click()
def main():
    for i in range(int(user_input1)):
        click()
user_input1 = input("Enter the ammount of clicks: ")
user_input2 = input("Enter a delay after each click: ")
user_input3 = input("Enter after how many second should the clicker be started after execution: ")
time.sleep(float(user_input3))
main()
print("Thank you for using the code :)")
