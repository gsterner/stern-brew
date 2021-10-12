import gravity
import constant_recipie as re

POUNDS_PER_KG = 2.20462
LITERS_PER_GALLON = 3.78541

def fermentable_contribution(points, mass, total_volume):
    return points * mass / total_volume

def convert_ppg_to_metric(ppg):
    return ppg * POUNDS_PER_KG * LITERS_PER_GALLON

def calculate_contribution(efficiency, gravity_ppg, mass, volume):
    gravity_metric = convert_ppg_to_metric(gravity_ppg)
    return fermentable_contribution(gravity_metric, mass, volume) * efficiency

#loop over fermentables
contribution = calculate_contribution(0.74,
                                      gravity.gravity["pale ale"],
                                      re.recipie["fermentables"]["pale ale"],
                                      re.recipie["volume"])
print(contribution)
