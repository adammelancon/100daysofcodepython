

# Get the info in "freedom units"
height_ft = input("enter your height in ft: ")
weight_lbs = input("enter your weight in lbs: ")

# Convert back to "science units"
height_m = (float(height_ft) / float(3.28))
weight_kg = int(weight_lbs) / 2.2046

# Calculate BMI
output = (weight_kg / (height_m ** 2))

if output <= 18.5:
  print("Your BMI is: " + str(int(output)) + ", you are underweight")
elif output <= 25:
  print("Your BMI is: " + str(int(output)) + ", you are normal weight")
elif output <= 30:
  print("Your BMI is: " + str(int(output)) + ", you are slightly overweight")  
elif output <= 35:
  print("Your BMI is: " + str(int(output)) + ", you are obese")
else:
  print("Your BMI is: " + str(int(output)) + ", you are clinically obese")
