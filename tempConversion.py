import tempConversion
def to_centigrade(x):
      return 5 * (x - 32) / 9.0
 
# function to convert C to F
def to_fahrenheit(x):
       return 9 * x / 5.0 + 32
 
# water freezing temperature(in Celsius)
FREEZING_C = 0.0 
 
# water freezing temperature(in Fahrenheit)     
FREEZING_F = 32.0     

print(tempConversion.to_centigrade(12))
print(tempConversion.FREEZING_F)

from tempConversion import to_fahrenheit
print(to_fahrenheit(20))

from tempConversion import FREEZING_C
print(FREEZING_C)
