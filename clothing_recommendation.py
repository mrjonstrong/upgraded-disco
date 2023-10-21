def get_clothing_recommendation(weather, temperature, precipitation):
    clothing = "Clothing: "

    if weather.lower() == "sunny":
        clothing += "Wear sunglasses, a hat, and sunscreen. "
        if temperature > 75:
            clothing += "Shorts and a t-shirt should be fine."
        elif temperature > 60:
            clothing += "A long sleeve shirt and pants should be comfortable."
        else:
            clothing += "Consider wearing a jacket."

    elif weather.lower() == "rainy":
        clothing += "Don't forget an umbrella or a raincoat. "
        if temperature > 75:
            clothing += "Shorts and a t-shirt should be fine underneath."
        elif temperature > 60:
            clothing += "A long sleeve shirt and pants should be comfortable."
        else:
            clothing += "Consider wearing a warm jacket."

    elif weather.lower() == "snowy":
        clothing += "Wear a heavy jacket, gloves, and a hat. "
        if precipitation > 50:
            clothing += "Snow boots are also recommended."
        else:
            clothing += "Warm shoes should be fine."

    elif weather.lower() == "cloudy":
        if temperature > 75:
            clothing += "Shorts and a t-shirt should be fine."
        elif temperature > 60:
            clothing += "A long sleeve shirt and pants should be comfortable."
        else:
            clothing += "Consider wearing a jacket."

    else:
        clothing += "Please check the entered weather condition."

    return clothing

def main():
    weather = input("Enter the current weather (sunny, rainy, snowy, cloudy): ")
    try:
        temperature = float(input("Enter the current temperature in Fahrenheit: "))
        precipitation = float(input("Enter the current precipitation percentage: "))
    except ValueError:
        print("Please enter valid numbers for temperature and precipitation.")
        return
    
    recommendation = get_clothing_recommendation(weather, temperature, precipitation)
    print(recommendation)

if __name__ == "__main__":
    main()