#!/usr/bin/env python3

# Exercise 17: Wi-Fi Diagnostic Tree
# This program leads the user through a series of steps to fix a Wi-Fi connection.

print("Reboot the computer and try to connect.")
answer = input("Did that fix the problem? (yes/no): ")

if answer == "no":
    print("Reboot the router and try to connect.")
    answer = input("Did that fix the problem? (yes/no): ")

    if answer == "no":
        print("Make sure the cables between" 
              "the router and modem are plugged in firmly.")
        answer = input("Did that fix the problem? (yes/no): ")

        if answer == "no":
            print("Move the router to a new location and try to connect.")
            answer = input("Did that fix the problem? (yes/no): ")

            if answer == "no":
                print("Get a new router.")
