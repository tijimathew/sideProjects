#test_example.py

import pytest
import example


class TestExample:
    
    def test_myFunctionWithValidInput(self):
        example.input = lambda _: "test"
        output = example.myFunction()
        assert output == True

    def test_myFunctionWithInvalidInput(self):
        example.input = lambda _: "foobar"
        output = example.myFunction()
        assert output == False

    def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
        example.input = input      