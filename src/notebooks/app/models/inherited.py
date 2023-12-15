#!/usr/bin/env python3



class Greeter:
    '''Base Class/Interface(kind of) Greeter'''
    
    def __init__(self, name):
        self.name = name

    def greet(self) -> None:
        '''Display a greeting message which properly introduces the current Person instance'''
        print(f"Hello! My name is {self.name} and it's a pleasure to meet you!")


class Leaver:
    '''Base Class/Interface(kind of) Leaver'''
    
    def __init__(self):
        # NOTE: use of the pass statement since there are no attribute/property assignments
        pass

    def leave(self) -> None:
        '''Display a good-bye message that politely leaves the room'''
        print("See you Space Cowboy!")


class SingleDerivedPerson(Greeter):
    '''Class SingleDerivedPerson - Derived Instance of Greeter Only'''
    
    def __init__(self, name="Unknown User"):
        super().__init__(name)



class CompoundDerivedPerson(Greeter, Leaver):
    '''Class CompoundDerivedPerson - Derived Shared Instance of Greeter and Leaver'''
    
    def __init__(self, name="Unknown User"):
        super().__init__(name)