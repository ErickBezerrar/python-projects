EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutes):
    """
    Calculate the remaining bake time.

    :param minutes: int - elapsed baking time.
    :return: int - remaining baking time.

    This function takes the elapsed baking time as input and calculates the remaining
    baking time by subtracting the elapsed time from the expected total baking time.
    """
    return EXPECTED_BAKE_TIME - minutes

def preparation_time_in_minutes(camadas):
    """
    Calculate the preparation time.

    :param camadas: int - number of layers.
    :return: int - total preparation time.

    This function calculates the total preparation time based on the number of layers
    specified for the lasagna. Each layer takes 2 minutes to prepare.
    """
    return camadas * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking. It calculates the total elapsed minutes spent cooking the
    lasagna by summing up the preparation time (2 minutes per layer) and the elapsed
    baking time.
    """
    return number_of_layers * 2 + elapsed_bake_time

# Example usages
print(bake_time_remaining(30))
print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(3, 20))
