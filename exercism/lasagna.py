EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutes):
    return EXPECTED_BAKE_TIME - minutes

def preparation_time_in_minutes(camadas):
    return camadas * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return number_of_layers * 2 + elapsed_bake_time
    
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
bake_time_remaining(30)
preparation_time_in_minutes(2)
elapsed_time_in_minutes(3, 20)
