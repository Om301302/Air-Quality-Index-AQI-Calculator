# Project 1

print('Air Quality Index Calculator')

location = input('What is the name of this location? \n')
#print()


# for the pm 2.5

pm25 = float(input('Enter PM-2.5 [ug/m3, 24-hr avg]: '))
if 0 <= pm25 <= 12.0 :
    ipm = (4.167 * ( pm25 - 0)) + 0
elif 12.1 <= pm25 <= 35.4 :
    ipm = (2.10 * ( pm25 - 12.1)) + 51
elif 35.5 <= pm25 <= 55.4 :
    ipm = (2.462 * (pm25 - 35.5)) + 101
elif 55.5 <= pm25 <= 150.4 :
    ipm = (0.516 * (pm25 - 55.5)) + 151
elif 150.5 <= pm25 <= 250.4 :
    ipm = (0.99 * (pm25 - 150.5)) + 201
elif 250.5 <= pm25 <= 500.4 :
    ipm = (0.796 * (pm25 - 250.5)) + 301
else:
    print('please enter a positive or valid number')

print(f'PM-2.5 concentration of {pm25:.1f} is index level {ipm:.0f}')
print()

#For the pm10
ipm1 = 0
pm10 = float(input('Enter PM-10 [ug/m3, 24-hr avg]: '))
if 0 <= pm10 <= 54 :
    ipm1 = ((50/54) * ( pm10 - 0)) + 0
elif 55 <= pm10 <= 154 :
    ipm1 = ((49/99) * ( pm10 - 55)) + 51
elif 155 <= pm10 <= 254 :
    ipm1 = ((49/99) * (pm10 - 155)) + 101
elif 255 <= pm10 <= 354 :
    ipm1 = ((49/99) * (pm10 - 255)) + 151
elif 355 <= pm10 <= 424 :
    ipm1 = ((99/69) * (pm10 - 355)) + 201
elif 425 <= pm10 <= 604 :
    ipm1 = ((199/179) * (pm10 - 425)) + 301
else:
    print('please enter a positive or valid number')

print(f'PM-10 concentration of {pm10:.0f} is index level {ipm1:.0f}')
print()

# for the NO2
ipm2 = 0
no2 = float(input('Enter NO-2 [ppb, 1-hr avg]: '))
if 0 <= no2 <= 53 :
    ipm2 = ((50/53) * ( no2 - 0)) + 0 
elif 54 <= no2 <= 100 :
    ipm2 = ((49/46) * ( no2 - 54)) + 51
elif 101 <= no2 <= 360 :
    ipm2 = ((49/259) * (no2 - 101)) + 101
elif 361 <= no2 <= 649 :
    ipm2 = ((49/288) * (no2 - 361)) + 151
elif 650 <= no2 <= 1249 :
    ipm2 = ((99/59 9) * (no2 - 650)) + 201
elif 1250 <= no2 <= 2049 :
    ipm2 = ((199/799) * (no2 - 1250)) + 301
else:
    print('please enter a positive or valid number')

print(f'NO-2 concentration of {no2:.0f} is index level {ipm2:.0f}')
print()


### comparison

if ipm >= ipm1 >= ipm2 or ipm >= ipm2>= ipm1 :
    a = ipm
    
elif ipm1 >= ipm >= ipm2 or ipm1 >= ipm2 >= ipm :
    a = ipm1
   
else :
    a = ipm2
    

## air quality checking

if 0 <= a <= 50 :
   print(f'AQI for CSULB Pyramid is {a:.0f}')
   print(f'Air Quality: Good')
elif 51 <= a <= 100 :
    print(f'AQI for CSULB Pyramid is {a:.0f}')
    print(f'Air Quality: Moderate')
elif 101 <= a <= 150 :
    print(f'AQI for CSULB Pyramid is {a:.0f}')
    print(f'Air Quality: Unhealthy for Sensitive Groups')
elif 151 <= a <=200 :
    print(f'AQI for CSULB Pyramid is {a:.0f}')
    print(f'Air Quality: Unhealthy')
elif 201 <= a <= 300 :
    print(f'AQI for CSULB Pyramid is {a:.0f}')
    print(f'Air Quality: Very Unhealthy')
else :
    print(f'AQI for {location} is {a:.0f}')
    print(f'Air Quality: Hazardous')


### -Om Kakadiya
## Thank you





