EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutos):
    print(EXPECTED_BAKE_TIME - minutos)

def preparation_time_in_minutes(camadas):
    print(camadas * 2)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    print(number_of_layers * 2 + elapsed_bake_time)