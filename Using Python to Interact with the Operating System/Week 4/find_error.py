#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors

  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)

  
  
### Some notes for myself: Break down of python file
# write a function error_search that takes log_file as a parameter and returns returned_errors
# The input() function takes the input from the user and then evaluates the expression. This means Python automatically identifies whether the user entered a string, a number, or a list. If the input provided isn't correct then Python will raise either a syntax error or exception. The program flow will stop until the user has given an input.
# We'll now read each log separately from the fishy.log file using the readlines() method.
#  For this, we'll create a list to store all the patterns (user input) that will be searched. This list is named error_patterns and, initially it has a pattern "error" to filter out all the ERROR logs only. You can change this to view other types of logs such as INFO and WARN. You can also empty initialize the list to fetch all types of logs, irrespective of their type.
# Now, let's use the search() method (present in re module) to check whether the file fishy.log has the user defined pattern and, if it is available, append them to the list returned_errors.
# Next, close the file fishy.log and return the results stored in the list returned_errors.
