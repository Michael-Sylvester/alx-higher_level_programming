Unit Testing Guidlines
Test Case Structure: Each test case should be a method within a class that inherits from unittest.TestCase. The method name should start with the word test.

Assertions: Use the various assertion methods provided by the unittest.TestCase class. These include methods like assertEqual(a, b), assertTrue(x), assertFalse(x), assertIn(a, b), and others.

Setup and Teardown: If there are repetitive tasks that need to be done before and after each test (like setting up mock data), you can use the setUp() and tearDown() methods.

Test Isolation: Each test should be independent of the others. This means a test should not rely on the state left by a previous test or change the state for the next tests.

Test Coverage: Try to cover as many edge cases and types of input as possible. This includes testing with normal inputs, boundary inputs, and invalid inputs.

Naming Conventions: Test method names should be descriptive so that it’s clear what each test does. A common practice is to use a name that describes the input and expected output.

Documentation: Each test should have a docstring briefly explaining what it tests.