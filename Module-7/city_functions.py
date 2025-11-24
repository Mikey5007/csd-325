# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a formatted city/country string with optional population and language."""

    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"

    if population:
        return f"{city.title()}, {country.title()} - population {population}"

    if language:
        return f"{city.title()}, {country.title()}, {language.title()}"

    return f"{city.title()}, {country.title()}"


# Call the function at least three times
city1 = input("Enter a city: ")
country1 = input("Enter the country for that city: ")
population1 = input("Enter the population (press Enter to skip): ")
language1 = input("Enter the language (press Enter to skip): ")
print(city_country(city1, country1, population1 if population1 else None, language1 if language1 else None))
print()   # blank line

city2 = input("Enter a second city: ")
country2 = input("Enter the country for that city: ")
population2 = input("Enter the population (press Enter to skip): ")
language2 = input("Enter the language (press Enter to skip): ")
print(city_country(city2, country2, population2 if population2 else None, language2 if language2 else None))
print()   # blank line

city3 = input("Enter a third city: ")
country3 = input("Enter the country for that city: ")
population3 = input("Enter the population (press Enter to skip): ")
language3 = input("Enter the language (press Enter to skip): ")
print(city_country(city3, country3, population3 if population3 else None, language3 if language3 else None))
print()   # blank line

input("\nPress Enter to exit...")

