import math
import pyjokes
# imagine that this is a very large application 

def area_circle(radius):
    return math.pi * radius ** 2.0 

def get_random_joke():
    joke = pyjokes.get_joke()
    return joke


