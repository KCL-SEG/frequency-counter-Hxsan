"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    # Converts all values in the list to a string
    items = [str(item) for item in items]

    # goes through each item of the list, adds an index if it doesnt exist - starting from 1
    for value in items:
        frequencies[value] = frequencies.get(value , 0) + 1
    
    return frequencies
