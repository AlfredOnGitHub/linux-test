import os
import pwd
import challenges

if __name__ == "__main__":
    while True:
        challenges.main_menu()
        choose = input('Which one do you want to do?: ')
        if int(choose) == int(1):
            challenges.fs('/this/is/test')
        elif int(choose) == int(2):
            challenges.check_users('test')
        elif int(choose) == int(3):
            challenges.security()
        elif int(choose) == int(4):
            challenges.package_mgmt()
        elif int(choose) == int(5):
            challenges.kernel_mgmt()
        elif int(choose) == int(6):
            challenges.log_mgmt()
        elif int(choose) == int(7):
            break
 