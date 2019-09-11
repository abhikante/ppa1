# PPA1

## Naming and Organizational Convention:
For all my tests, I followed the same format for naming. The name always starts with "test_" followed by a short form of the name of the function I'm testing and then a brief one or two word description of what my test is doing. For example, my first test checks whether my BMI function returns a float, so it will be named "test_bmi_nonfloat()", since the test is checking whether my program throws an error when a non-float value is provided.

## Setup and Execution:
1. Download the latest version of Python (v3.7.4): https://www.python.org/downloads/release/python-374/
2. In a command prompt, execute the following command: "pip install -U pytest". This installs the pytest framework that I used in this project.
3. Download my files off GitHub into a single folder.
4. To run my test file, navigate to the folder in which my files are located in command prompt and simply run the command "pytest -v". The command automatically runs all test files in the provided folder.
5. To run the main function file, execute the command "python ppa1.py" in the same folder. The program should run successfully!

## Screenshot of Tests Passing
![Screenshot](https://github.com/abhikante/ppa1/blob/master/Tests_Passing.PNG)

## Unit Testing Experience
I feel that I was able to do my project very efficiently using the TDD approach. Everything moved in a very straightforward fashion, where I would first determine what was needed from my function, write the test for that function, then write the implementation of that function. Following this method made my programming process very clear and I always had a good idea of what I needed to do next. I certainly think it will be useful for a real project; often times when I program, I move around my program a lot and tend to get lost. The TDD approach seemed to have prevented this problem for the most part and made my programming process very structural. One drawback I found of TDD however was that it was very time-consuming. When I was working on a function in this structured way and got stuck at a problem, I had to pretty much halt everything I was doing to figure out this one problem; in a non-TDD environment, I would have simply moved on to something else I knew I could accomplish and then later return to this problem.
