# PPA1

## Naming and Organizational Convention:
For all my tests, I followed the same format for naming. The name always starts with "test_" followed by a short form of the name of the function I'm testing and then a brief one or two word description of what my test is doing. For example, my first test checks whether my BMI function returns a float, so it will be named "test_bmi_nonfloat()", since the test is checking whether my program throws an error when a non-float value is provided.

## Setup and Execution:
1. Download the latest version of Python (v3.7.4): https://www.python.org/downloads/release/python-374/
2. In a command prompt, execute the following command: "pip install -U pytest". This installs the pytest framework that I used in this project.
3. Download my files off GitHub into a single folder.
4. To run my test file, navigate to the folder in which my files are located in command prompt and simply run the command "pytest". The command automatically runs all test files in the provided folder.
5. To run the main function file, execute the command "python ppa1.py" in the same folder. The program should run successfully!

## Screenshot of Tests Passing
