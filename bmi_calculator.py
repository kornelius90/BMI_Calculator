def calculate_bmi(weight, height):
    """Calcul BMI: weight în kilograme și height în metri."""
    return weight / (height ** 2)

def main():
    try:
        weight = float(input("Introduceți greutatea (kg): "))
        height = float(input("Introduceți înălțimea (m): "))
        
        bmi = calculate_bmi(weight, height)
        print(f"BMI-ul calculat este: {bmi:.2f}")
        
        if bmi < 18.5:
            print("Subponderal")
        elif 18.5 <= bmi < 24.9:
            print("Greutate normală")
        elif 25 <= bmi < 29.9:
            print("Supraponderal")
        else:
            print("Obezitate")
            
    except ValueError:
        print("Vă rugăm să introduceți valori numerice valide.")

if __name__ == "__main__":
    main()
