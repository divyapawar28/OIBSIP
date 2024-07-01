def calculator_bmi(weight_kg, height_cm) :
     height_m = height_cm /100       #convert height in metres
     bmi = weight_kg / (height_m ** 2)
     return bmi

def classify_bmi(bmi_value) :
     if bmi_value < 16 :
          return " Severly Underweight"
     
     elif 16 <= bmi_value < 18.5 :
          return "Underweight"
     
     elif 18.5 <= bmi_value < 25 :
          return "Healthy"
     
     elif 25 <= bmi_value < 30 :
          return "Overweight"
     
     else : 
          return "Obese"
     
def main() :
          weight = float(input("Enter your weight in kilograms (kg) : "))
          height = float(input("Enter yoyr height in centimeters (cm) : "))
          
          bmi_result = calculator_bmi(weight, height)
          category = classify_bmi(bmi_result)
          
          print(f"Your BMI is {bmi_result : .2f}")
          print(f"This is considered : {category}")
          
if __name__ == "__main__" : 
     main()
     
     
     
