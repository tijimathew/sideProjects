#test_example.py

import pytest
import example


class TestClass:
    
    def test_myFunctionWithValidMockUserInput(self):
        example.input = lambda _: "test"
        output = example.myFunction()
        assert output == "test"

    def test_myFunctionWithInvalidMockUserInput(self):
        example.input = lambda _: "foobar"
        output = example.myFunction()
        assert output != "test"

    def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
        example.input = input      