from unittest.mock import Mock
from unittest.mock import create_autospec


def print_header(number):
    print('===== Question {no} ====='.format(no=number))


# Question 1
# preconfigure m1 so it has a method called 'run'
# preconfigure m1 so it returns 5
print_header(1)
m1 = Mock()
attributes = {
    'run.return_value': 5,
}
m1.configure_mock(**attributes)
result = m1.run()
print(str(result))

# Question 2
# call m1.run() with 1, 3, 5, 7 
# call m1.run () with 2, 4, 6
# What's the results?

print_header(2)
for i in [1, 3, 5, 7]:
    print(m1.run(i))
for i in [2, 4, 6]:
    print(m1.run(i))

# Question 3
# pass m1 to the dir() function.
# which attribute verifies how many times m1 is called?
print_header(3)
print(dir(m1))
# should be 'call_count'

# Question 4
# update m1.run() so it now returns [1, 2, 3]
# use return_value attribute for this
attributes = {
    'run.return_value': [1, 2, 3],
}
m1 = Mock(**attributes)

# Question 5
# Test that you re-configured m1 correctly. Call m1.run()
print_header(5)
print(str(m1.run()))

# Question 6
# Use dir(m1) to see teh functionality of the mock object again
# call assert_called and assert_called_once
# What's the output? Keep notes of this
print_header(61)
print(dir(m1))
print_header(62)
print(m1.run.assert_called())
print_header(63)
print(m1.run.assert_called_once())

# Question 7

# Create a simple function with the following details:

"""
def function(a, b, c):
    return a + b + c  
"""

# Use unittest.mock to ensure that the mock object is called correctly
# I.e, the following should product an error
# >>> m1(1)
# >>> m1(5, 10)
# The following should NOT
# >>> m1(1, 2, 3)
# If stuck, read: https://docs.python.org/3/library/unittest.mock.html 
