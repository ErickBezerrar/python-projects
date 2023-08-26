import lasagna
from lasagna import bake_time_remaining
from lasagna import preparation_time_in_minutes
from lasagna import elapsed_time_in_minutes

print(lasagna.EXPECTED_BAKE_TIME)

bake_time_remaining(30)
preparation_time_in_minutes(2)
elapsed_time_in_minutes(3, 20)

