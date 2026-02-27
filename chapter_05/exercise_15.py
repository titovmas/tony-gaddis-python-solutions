#!/usr/bin/env python3

# Exercise 15: Test Average and Grade
# This program calculates grades for five tests and their average.

def main():
    # Get five test scores from the user
    score1 = float(input("Enter score for test 1: "))
    score2 = float(input("Enter score for test 2: "))
    score3 = float(input("Enter score for test 3: "))
    score4 = float(input("Enter score for test 4: "))
    score5 = float(input("Enter score for test 5: "))

    # Display scores and grades for each test
    print("\nResults:")
    print(f"Test 1: {score1} - {determine_grade(score1)}")
    print(f"Test 2: {score2} - {determine_grade(score2)}")
    print(f"Test 3: {score3} - {determine_grade(score3)}")
    print(f"Test 4: {score4} - {determine_grade(score4)}")
    print(f"Test 5: {score5} - {determine_grade(score5)}")

    # Calculate and display the average
    avg = calc_average(score1, score2, score3, score4, score5)
    print(f"\nAverage Score: {avg:.2f}")
    print(f"Average Grade: {determine_grade(avg)}")

def calc_average(s1, s2, s3, s4, s5):
    # Calculate the average of five scores
    return (s1 + s2 + s3 + s4 + s5) / 5

def determine_grade(score):
    # Determine the letter grade based on the score
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Call the main function
main()
