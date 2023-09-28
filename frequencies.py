"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    items = [str(item) for item in items]

    for value in items:
        frequencies[value] = frequencies.get(value , 0) + 1
    
    return frequencies
