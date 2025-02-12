spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
#takes a list of spicy foods and  returns a list of strings with the names of each spicy food
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

 #Returns a list of dictionaries of spicy foods where the heat level is greater than 5.
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

#Prints each spicy food in the format: Name (Cuisine) | Heat Level: 🌶 (repeated by heat level).
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_icons = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_icons}")

#Returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

#Outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_icons = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_icons}")

#Returns an integer representing the average heat level of all the spicy foods in the array.
def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  # Handle empty list case to avoid division by zero

    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

#Returns the original list with the new spicy_food added.
def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
