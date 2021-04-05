"""
CISC 140 Midterm Exam Test Client

This program will perform a variety of tests upon your implementation of DArray
to ensure that it complies with the API specified in the midterm examination
document. It will also display an estimate of your grade at completion, based
on how many tests your code passes/fails. Please note that this estimate is a
maximum value for your grade, and your actual grade may be lower, depending on
the way that you've written your code (which can't actually be assessed by this
test client).

Please note that the client that will be used to test your code for grading
purposes will contain the same tests, but use slightly different inputs, to
prevent you from writing a class that "fakes" passing the tests by only giving
what you know the test is going to expect.

DO NOT MAKE ANY MODIFICATIONS TO THIS CLIENT WHATSOEVER. If a test fails, the
problem is with your code, not the client. Modify your class to fix the issue,
rather than modifying the test client so that your code passes. Any
modifications that you make to the test client will not be used during grading.
"""

import random
import sys
import os
import stdio
import math
from instream import InStream
from darray import DArray # Ensure that your file is called darray.py and that
                          # it is in the same directory as this test client.

def main():
    total_tests = 30
    total_score = 220
    score = 0 # running tally of points earned for passing each test.
    tests_passed = 0 # running tally of tests passed

    # Create an empty darray object
    stdio.write("Calling Constructor w/o argument:\t\t\t\t")
    try:
        array = DArray()
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[10/10 points]")
        score += 10
    except:
        stdio.writeln("failed")
        stdio.writeln("[0/10 points]")
        stdio.writeln("Cannot build object; no further tests can be run.")
        stdio.writeln("Bailing out...")
        sys.exit(-1)


    # test length (should be 0 for empty array)
    stdio.write("Testing empty array length (should be 0):\t\t\t")
    if len(array) == 0:
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5
    else:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")


    # test string representation (should be '[]' for empty array)
    stdio.write("Testing string representation (should be []):\t\t\t")
    if str(array) == '[]':
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[10/10 points]")
        score += 10
    else:
        stdio.writeln("failed.")
        stdio.writeln("[0/10 points]")


    # test accessing first element (should raise index error)
    stdio.write("Testing first element access (should raise IndexError):\t\t")
    try:
        array[0]
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")

    except IndexError:
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")

    # test assigning first element (should raise index error)
    stdio.write("Testing assigning to first element (should raise IndexError):\t")
    try:
        array[0] = "test"
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")
    except IndexError:
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")


    # test adding an element
    stdio.write("Testing addelem:\t\t\t\t\t\t")
    e = "test element" # this value will change for grading
    try:
        array.addelem(e)
        tests_passed += 1
        stdio.writeln("passed.")
        stdio.writeln("[10/10 points]")
        score += 10
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/10 points]")

    # test length update
    stdio.write("Testing array length increase:\t\t\t\t\t")
    if len(array) == 1:
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[10/10 points]")
        score += 10
    else:
        stdio.writeln("failed.")
        stdio.writeln("[0/10 points]")

    # test element access
    stdio.write("Testing accessing added element:\t\t\t\t")
    try:
        x = array[0]
        stdio.writeln("passed.")
        stdio.writeln("[5/5 points]")
        score += 5
        tests_passed += 1
        # test element correctness
        stdio.write("Accessed element is same as added one:\t\t\t\t")
        if x == e:
            stdio.writeln("passed.")
            tests_passed += 1
            stdio.writeln("[10/10 points]")
            score += 10
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/10 points]")


        stdio.write("String representation is correct:\t\t\t\t")
        if str(array) == "[" + repr(e) + "]":
            stdio.writeln("passed.")
            tests_passed += 1
            stdio.writeln("[5/5 points]")
            score += 5
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/5 points]")
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")
        stdio.writeln("Accessed element is same as added one:\t\t\t\tfailed.")
        stdio.writeln("String representation is correct:\t\t\t\tfailed.")


    # test element update
    stdio.write("Testing assignment to added element:\t\t\t\t")
    try:
        e = 1234 # this value will change for grading
        array[0] = e
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5

        stdio.write("Assignment properly updated element:\t\t\t\t")
        if array[0] == e:
            stdio.writeln("passed.")
            tests_passed += 1
            stdio.writeln("[10/10 points]")
            score += 10
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/10 points]")

        stdio.write("String representation is correct:\t\t\t\t")
        if str(array) == "[" + repr(e) + "]":
            stdio.writeln("passed.")
            tests_passed += 1
            stdio.writeln("[5/5 points]")
            score += 5
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/5 points]")

    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")
        stdio.writeln("Assignment properly updated element:\t\t\t\tfailed.")
        stdio.writeln("[0/5 points]")



    stdio.write("Adding lots of elements to array:\t\t\t\t")
    cnt = random.randint(10000, 15000) # this number may be changed while grading
    try:
        for i in range(cnt):
            array.addelem(random.randint(0, 100))
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[15/15 points]")
        score += 15
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/15 points]")

    stdio.write("Verifying length after adding elements:\t\t\t\t")
    if len(array) == cnt + 1:
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5
    else:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")


    stdio.write("Verifying assignment to last element in array:\t\t\t")
    e = "test"
    try:
        array[len(array) - 1] = e
        stdio.writeln("passed.")
        stdio.writeln("[5/5 points]")
        score += 5
        tests_passed += 1

        stdio.write("Verifying assigned value:\t\t\t\t\t")
        if array[len(array) - 1] == e:
            stdio.writeln("passed.")
            tests_passed += 1
            stdio.writeln("[5/5 points]")
            score += 5
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/5 points]")

    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")
        stdio.writeln("Verifying assigned value:\t\t\t\t\tfailed.")
        stdio.writeln("[0/5 points]")


    stdio.writeln('-'*71)

    # Test creating darray from existing array
    stdio.write("Creating darray from existing array:\t\t\t\t")
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # this value may change when grading
    try:
        array = DArray(x)
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5
    except:
        stdio.writeln("failed")
        stdio.writeln("Cannot build object; no further tests can be run.")
        stdio.writeln("Bailing out...")
        sys.exit(-1)

    stdio.write("Verifying elements in darray are same as in existing:\t\t")
    for i in range(len(array)):
        if array[i] == x[i]:
            pass
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/5 points]")
    else:
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5

    stdio.write("Verifying darray contains copy of existing:\t\t\t")
    x[0] = "test" # this value may change when grading
    if array[0] == x[0]:
        stdio.writeln("failed.")
        stdio.writeln("[0/10 points]")
    else:
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[10/10 points]")
        score += 10

    stdio.write("Adding lots of elements to array:\t\t\t\t")
    cnt = random.randint(10000, 15000) # this number may be changed while grading
    try:
        for i in range(cnt):
            array.addelem(random.randint(0, 100))
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[10/10 points]")
        score += 10
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/10 points]")

    stdio.write("Verifying length after adding elements:\t\t\t\t")
    if len(array) == cnt + len(x):
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5
    else:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")


    stdio.writeln('-'*71)


    try:
        fil = InStream('numbers.dat') # the data in this file will change when grading
    except:
        stdio.writeln("ERROR: Ensure that numbers.dat is in your working directory.")
        stdio.write("This is NOT an issue with your code.\nPlease put numbers.dat ")
        stdio.writef("into this directory: [%s] \nand try again.\n", os.getcwd())
        sys.exit(-1)

    stdio.write("Creating new empty DArray and filling with data from file:\t")
    try:
        array = DArray()
        while not fil.isEmpty():
            array.addelem(fil.readFloat())

        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[15/15 points]")
        score += 15
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/15 points]")
        stdio.writeln("Cannot build object; no further tests can be run.")
        stdio.writeln("Bailing out...")
        sys.exit(-1)

    stdio.write("Calculating average of numbers in the array:\t\t\t")
    true_average = 836.65
    acc = 0
    try:
        for num in array:
            acc += num
        average = acc / len(array)

        if math.isclose(average, true_average, abs_tol=.1):
            stdio.writeln("passed.")
            stdio.writeln("[10/10 points]")
            score += 10
            tests_passed += 1
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/10 points]")
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/10 points]")


    stdio.writeln('-'*71)

    stdio.write("Creating darray with empty array as input:\t\t\t")
    try:
        array = DArray([])
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5

        stdio.write("Verifying length is 0:\t\t\t\t\t\t")
        if len(array) == 0:
            stdio.writeln("passed.")
            tests_passed += 1
            stdio.writeln("[5/5 points]")
            score += 5
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/5 points]")
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")
        stdio.writeln("Verifying length is 0:\t\t\t\t\t\tfailed.")
        stdio.writeln("[0/5 points]")


    stdio.write("Adding elements to darray:\t\t\t\t\t")
    try:
        array.addelem("123")
        array.addelem("456")
        array.addelem(True)
        array.addelem("y")
        array.addelem(3.14)
        array.addelem(None)
        array.addelem("test")

        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5
    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")
        stdio.writeln("Cannot build object; no further tests can be run.")
        stdio.writeln("Bailing out...")
        sys.exit(-1)

    stdio.write("Verifying str of darray:\t\t\t\t\t")
    s = "['123', '456', True, 'y', 3.14, None, 'test']"
    if str(array) == s:
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[5/5 points]")
        score += 5
    else:
        stdio.writeln("failed.")
        stdio.writeln("[0/5 points]")


    stdio.write("Verifying assignment to darray:\t\t\t\t\t")
    try:
        array[3] = 5
        stdio.writeln("passed.")
        tests_passed += 1
        stdio.writeln("[10/10 points]")
        score += 10

        stdio.write("Verifying new str of darray:\t\t\t\t\t")
        s = "['123', '456', True, 5, 3.14, None, 'test']"

        if str(array) == s:
            stdio.writeln("passed.")
            tests_passed += 1
            stdio.writeln("[5/5 points]")
            score += 5
        else:
            stdio.writeln("failed.")
            stdio.writeln("[0/5 points]")

    except:
        stdio.writeln("failed.")
        stdio.writeln("[0/10 points]")


    stdio.writeln('-'*71)


    stdio.writef("%7d tests passed.\n", tests_passed)
    stdio.writef("%7d tests failed.\n", total_tests - tests_passed)
    stdio.writef("%7.2f percent pass rate.\n", tests_passed / total_tests * 100)
    stdio.writeln()
    stdio.writef("%7d points earned.\n", score)
    stdio.writef("%7d points missed.\n", total_score - score)
    stdio.writef("%7.2f percent score.\n", score / total_score * 100)


if __name__ == '__main__':
    main()
