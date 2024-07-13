import os
name = input("What is your name?\n")        # Input function give name from user
know_python = input("Do you know python? \n") # Enter (Yes/No)
print("Thanks for answering my question, ", name, "\n") # Output function
print("The current Directory is ", os.getcwd()) # prints the cwd path.

""" This is a basic input and output program.

  The os (Operating System) module in Python is a built-in library that provides functions
   for interacting with the operating system. It allows you to perform a wide variety of tasks,
  such as reading and writing files, interacting with the file system, and running system commands.

        import os is Python statement which is used for include os module in your script.

         os.getcwd() {get current working directory} shows the current working directory.

Date: 02/07/2024

Developer Name : Mr. Error 313
"""
