#!/usr/bin/env python3


# 2-3 lines between class definitions per PEP guidelines
# at least 1 line between specific sections to maintain readability
# NOTE: (I don't really know or care and that's the point.) We'll rely heavily on a linter to standardize our code per PEP guidelines once the code exists. Then you can tweak your pre-commit settings however you like.
class Person:
    '''Base Class Person'''

    # NOTE: the above string is called a docstring and is viewable via interactive sessions in the python interpreter
    def __init__(self, name="Unknown User"):
        self.name = name
    
    # type-hint a return type for our function using the syntax:
    # `def method(self) -> datatype`
    # NOTE 1: the first argument of any class method will usually be the special keyword `self`
    # NOTE 2: Note 1 may be incorrect if it's a static method (I can't really remember right now)
    def greet(self) -> None:
        '''Display a greeting message which properly introduces the current Person instance'''
        # class attributes are accessed via self.variable_name
        print(f"Hello! My name is {self.name} and it's a pleasure to meet you!")