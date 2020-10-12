# Lab 42: Pythonisms

## Overview
- Python has many elegant features that can show the difference between a “programmer who uses Python” and a true “Pythonista”

- Pythonista may be a silly word but it’s a real thing. A true pythonista is able to leverage the particular features of Python to accomplish a task in a simpler and more easy to reason about way.

## Dunder Methods

- These “dunders” or “special methods” in Python are also sometimes called “magic methods.” But using this terminology can make them seem more complicated than they really are—at the end of the day there’s nothing “magical” about them. You should treat these methods like a normal language feature.

## Iterators
- Iterators provide a sequence interface to Python objects that’s memory efficient and considered Pythonic. Behold the beauty of the for-in loop!

- To support iteration an object needs to implement the iterator protocol by providing the iter and next dunder methods.

- Class-based iterators are only one way to write iterable objects in Python. Also consider generators and generator expressions.

## Generators
- Generators are a tricky subject in Python. With this tutorial you’ll make the leap from class-based iterators to using generator functions and the “yield” statement in no time.
- Generator functions are syntactic sugar for writing objects that support the iterator protocol. Generators abstract away much of the boilerplate code needed when writing class-based iterators.
- The yield statement allows you to temporarily suspend execution of a generator function and to pass back values from it.
- Generators start raising StopIteration exceptions after control flow leaves the generator function by any means other than a yield statement.
- A generator is implemented with a syntax that is very similar to a function, but instead of returning values, a yield statement is executed to indicate each element of the series.
## Decorators
- Create a decorator that adds behavior to a given function: Convert the return value in some way

### Estimated time to finish the lab: 2 hours
### Actual time needed to finish the lab:1-1.5 hours
### Start time: 3:00 PM
### Finish time:4:30 PM
