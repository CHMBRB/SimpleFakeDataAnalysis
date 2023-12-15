#!/usr/bin/env python3



class Signals:
    '''A Refactored and Renamed Base Class/Interface(kind of) To Replace Greeter and Leaver Classes'''
    
    def __init__(self, name):
        self.name = name

    def greet(self) -> None:
        '''Display a greeting message which properly introduces the current Person instance'''
        print(f"Hello! My name is {self.name} and it's a pleasure to meet you!")
    
    def leave(self) -> None:
        '''Display a good-bye message that politely leaves the room'''
        print(f"See you Space Cowboy! Signing off. - {self.name}")


class Person:
    '''Base Class Person - Dependency Injected Implementation of Person'''

    # private variable/attribute declaration syntax to demonstrate intent
    _signals: Signals
    
    # it's probably a good idea to type-hint when using DI
    def __init__(self, signals:Signals):
        self._signals = signals

    # while we may already access signals using `self._signals.greet()`, `self._signals.leave()`, or `self._signals.name` that's not proper convention for "private" methods/variables
    # instead, we'll expose similarly named public methods which reference those private object methods
    def greet(self) -> None:
        '''Call Signals.greet() private method'''
        self._signals.greet()
    
    def leave(self) -> None:
        '''Call Signals.leave() private method'''
        self._signals.leave()

    def name(self) -> str:
        '''Call to Signals.name property; returns String'''
        return self._signals.name