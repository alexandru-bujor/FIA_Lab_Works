import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "task2_rules")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "task5_question_generation")))

# TODO: add your imports here:
# from rules import my_rules


if __name__=='__main__':

    #TODO: implement your code here!
    
    # example how to print output:
    print("Welcome to Expert System! TODO: implement")

    # an example how to read input:
    input_name = input("please write your name:\n")

    print("Hello, ", input_name, "!")

    # example how to read a numeric input:
    input_age = int(input("what is your age?\n"))
    print("Your age is", input_age)

    print("Great! Now please implement the code for the lab :) ")
