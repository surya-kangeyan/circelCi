import algebra 
import rest_api_server
import math
import pyjokes

def test_area_circle():
    area = algebra.area_circle(100)
    assert math.isclose(area, 31415.926535897932)

def test_random_joke():
    joke = pyjokes.get_joke()
    # Check that the joke is a non-empty string
    assert isinstance(joke, str), "Joke should be a string"
    assert len(joke) > 0, "Joke should not be an empty string"
    
    # Optionally, verify the joke is part of the pyjokes collection
    jokes_list = pyjokes.get_jokes()
    assert joke in jokes_list, "Joke should be a valid joke from pyjokes"