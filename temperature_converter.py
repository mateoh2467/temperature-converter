print("Welcome to temperature converter, a lightweight utiity for converting temperatures. ")

#Create variables for the unit that's being converted and the temperature
unit = input("Please specify the temperature you want converted: ").upper()
value = float(input("Please specify the temperature you want converted: "))

#Function that converts C to F 
def c_to_f(temp_c):
    converted_c = temp_c * (9/5) + 32
    return converted_c

#Function that converts F to C
def f_to_c(temp_f):
    converted_f = (temp_f - 32) * (5/9) 
    return converted_f

#Main function that uses conditionals to decide which convert function to select 
def main():
    if(unit == "C"):
        celsius_to_fahrenheit = c_to_f(value)
        return celsius_to_fahrenheit
    elif(unit == "F"):
        fahrenheit_to_celsius = f_to_c(value)
        return fahrenheit_to_celsius
    else:
        warning = "Please enter C or F to specify the unit: "
        return warning 

#Print results
result = main()
print("Your value is: " + str(result))