"""
This module provides a CLI application for recommending clothing based on the current weather, 
temperature, and precipitation. The application's complexity is reduced by using functions 
and dictionaries to handle different weather conditions and recommendations.
"""

def sunny_clothing(temperature):
    """
    Provides clothing recommendation for sunny weather based on the temperature.
    
    Parameters:
    - temperature (float): The current temperature in Fahrenheit.
    
    Returns:
    - str: A string containing the clothing recommendation for sunny weather.
    """
    if temperature > 75:
        return "Shorts and a t-shirt should be fine."
    elif temperature > 60:
        return "A long sleeve shirt and pants should be comfortable."
    else:
        return "Consider wearing a jacket."

def rainy_clothing(temperature):
    """
    Provides clothing recommendation for rainy weather based on the temperature.
    
    Parameters:
    - temperature (float): The current temperature in Fahrenheit.
    
    Returns:
    - str: A string containing the clothing recommendation for rainy weather.
    """
    if temperature > 75:
        return "Shorts and a t-shirt should be fine underneath."
    elif temperature > 60:
        return "A long sleeve shirt and pants should be comfortable."
    else:
        return "Consider wearing a warm jacket."

def snowy_clothing(precipitation):
    """
    Provides clothing recommendation for snowy weather based on the precipitation.
    
    Parameters:
    - precipitation (float): The current precipitation percentage.
    
    Returns:
    - str: A string containing the clothing recommendation for snowy weather.
    """
    if precipitation > 50:
        return "Snow boots are also recommended."
    else:
        return "Warm shoes should be fine."

def cloudy_clothing(temperature):
    """
    Provides clothing recommendation for cloudy weather based on the temperature.
    
    Parameters:
    - temperature (float): The current temperature in Fahrenheit.
    
    Returns:
    - str: A string containing the clothing recommendation for cloudy weather.
    """
    if temperature > 75:
        return "Shorts and a t-shirt should be fine."
    elif temperature > 60:
        return "A long sleeve shirt and pants should be comfortable."
    else:
        return "Consider wearing a jacket."

WEATHER_CLOTHING_MAP = {
    "sunny": ("Wear sunglasses, a hat, and sunscreen. ", sunny_clothing),
    "rainy": ("Don't forget an umbrella or a raincoat. ", rainy_clothing),
    "snowy": ("Wear a heavy jacket, gloves, and a hat. ", snowy_clothing),
    "cloudy": ("", cloudy_clothing),
}

def get_clothing_recommendation(weather, temperature, precipitation):
    """
    Determine appropriate clothing based on the weather, temperature, and precipitation.
    
    Parameters:
    - weather (str): Current weather condition (sunny, rainy, snowy, cloudy).
    - temperature (float): Current temperature in Fahrenheit.
    - precipitation (float): Current precipitation percentage.
    
    Returns:
    - str: A string containing the clothing recommendation.
    """
    
    base_clothing, func = WEATHER_CLOTHING_MAP.get(weather.lower(), (None, None))
    if base_clothing is None:
        return "Clothing: Please check the entered weather condition."
    
    clothing = "Clothing: " + base_clothing
    
    if weather.lower() == "snowy":
        clothing += func(precipitation)
    else:
        clothing += func(temperature)
    
    return clothing

def main():
    """
    Execute the main program to ask the user for weather details and provide clothing 
    recommendations.
    """

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
