# Blutalkoholrechner v1.0
# by Lorenz Holstein
import time

#Variables
volume = 0
alcVolume = 0
mass = 0
gender = 0

alcMass = 0
bak = 0

#Inputs
volume = int(input("Getränkvolumen in [ml]: ")) 
alcVolume = int(input("Volumenprozent in [%]: "))
mass = float(input("Körpermasse in [kg]: "))
while gender not in (1,2):
    gender = int(input("Geschlecht; [1]weiblich  [2]männlich: "))

#Alcohol Mass
alcMass = volume * (alcVolume / 100) * 0.875 #Calculate mass of Ethanol in Drink

#Alcohol in Blood
if gender == 1:
    bak = alcMass / (mass * 0.55)
else:
    bak = alcMass / (mass * 0.68)
#Output
print('\n\n')
print('+++++++++++++++++++++++++++++++')
print(round(bak, 3), 'Promille')
print(round(alcMass, 3), 'g reiner Alkohol im Blut')
print('+++++++++++++++++++++++++++++++')

time.sleep(10)