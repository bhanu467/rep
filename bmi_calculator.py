def bmi_cal(weight, height, age):
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Input validation for weight and height
    if weight <= 0 or height <= 0:
        return "Error: Weight and height must be positive numbers!"
    
    # Provide BMI category and advice based on BMI value
    if bmi < 18.5:
        category = "Underweight"
        advice = "It’s important to focus on gaining some healthy weight. Include more protein and calorie-rich foods in your diet."
        activity = "Consider low-impact exercise like walking or swimming to stay active."
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
        advice = "Great job! Keep up the balanced diet and regular physical activity to maintain your current weight."
        activity = "Continue with moderate exercises like jogging or cycling to stay fit."
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
        advice = "It’s important to focus on losing some weight. Aim for a balanced diet and regular physical activity."
        activity = "Try to incorporate more cardio exercises like running or brisk walking."
    else:
        category = "Obese"
        advice = "It’s important to consult a healthcare provider to create a personalized weight loss plan."
        activity = "Focus on high-intensity interval training (HIIT) and other fat-burning exercises with professional guidance."
    
    # Provide advice based on age
    if age < 18:
        age_group_advice = "As you're still growing, make sure to focus on a balanced diet with proper nutrients."
    elif 18 <= age <= 40:
        age_group_advice = "In this age group, maintaining a healthy lifestyle is crucial. Keep exercising regularly and eating a balanced diet."
    elif 41 <= age <= 60:
        age_group_advice = "As you age, make sure to include joint-friendly exercises like walking or yoga to maintain flexibility."
    else:
        age_group_advice = "At this stage, focus on exercises that improve strength and bone density. Consult with a doctor for personalized advice."

    # Print the results
    print(f"\n--- BMI Report ---")
    print(f"Weight: {weight} kg\nHeight: {height} m\nAge: {age} years")
    print(f"BMI: {round(bmi, 2)}")
    print(f"Category: {category}")
    print(f"Advice: {advice}")
    print(f"Activity Recommendation: {activity}")
    print(f"Additional Advice for Your Age: {age_group_advice}")
    
    return bmi


def bmi_history():
    history = []  # List to store previous BMI checks
    
    while True:
        # Collect user information
        try:
            weight = float(input("\nEnter your weight (in kg): "))
            height = float(input("Enter your height (in meters): "))
            age = int(input("Enter your age (in years): "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue
        
        # Call the BMI calculation function
        bmi_value = bmi_cal(weight, height, age)
        
        # Store the result in history
        history.append((weight, height, age, bmi_value))
        
        # Ask the user if they want to check another BMI
        cont = input("\nWould you like to check another BMI? (yes/no): ").lower()
        if cont != "yes":
            break
    
    # Display history of BMI checks
    print("\n--- BMI History ---")
    for idx, record in enumerate(history, 1):
        weight, height, age, bmi_value = record
        print(f"{idx}. Weight: {weight} kg, Height: {height} m, Age: {age} years, BMI: {round(bmi_value, 2)}")


# Main loop to start the program
def main():
    print("Welcome to the BMI Calculator!")
    
    while True:
        # Ask user what they want to do
        choice = input("\nWould you like to (1) Calculate your BMI or (2) View BMI History (or 'exit' to quit): ").lower()
        
        if choice == '1':
            weight = float(input("\nEnter your weight (in kg): "))
            height = float(input("Enter your height (in meters): "))
            age = int(input("Enter your age (in years): "))
            bmi_cal(weight, height, age)
        
        elif choice == '2':
            bmi_history()
        
        elif choice == 'exit':
            print("\nThank you for using the BMI Calculator. Goodbye!")
            break
        
        else:
            print("\nInvalid choice! Please choose 1 to calculate BMI, 2 to view BMI history, or 'exit' to quit.")


if __name__ == "__main__":
    main()
