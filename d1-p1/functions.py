
def calcTotalFuel(mass):
    total_fuel = 0
    last_fuel = calcFuelPerUnitMass(mass)
    while(last_fuel >= 0):
        total_fuel = total_fuel + last_fuel
        last_fuel = calcFuelPerUnitMass(last_fuel)
    return total_fuel
    
def calcFuelPerUnitMass(mass):
    return int(mass / 3) - 2
