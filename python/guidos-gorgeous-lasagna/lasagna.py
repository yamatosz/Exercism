"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time_actual):
    """
    Return how much time is left to bake a lasagna 
    based on the time that has already been in the oven and the time required
    """
    return EXPECTED_BAKE_TIME - time_actual

def preparation_time_in_minutes(layers):
    """
    Returns the time spent preparing the 
    lasagna based on the layers the lasagna has
    """
    return layers * 2 

def elapsed_time_in_minutes(layers, time_actual):
    """ 
    Returns the total amount of time 
    spent based on prep time and the time the lasagna has been in the oven

    Receive the amount of layers and the time the lasagna has ben in the oven
    """
    return preparation_time_in_minutes(layers) + time_actual