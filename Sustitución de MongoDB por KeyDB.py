import redis

# Configuración de la conexión a KeyDB
REDIS_HOST = "localhost"
REDIS_PORT = 6379

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def add_recipe():
    name = input("Enter recipe name: ").strip()
    ingredients = input("Enter ingredients (comma-separated): ").strip()
    steps = input("Enter steps (separated by periods): ").strip()

    recipe_data = {
        "ingredients": ingredients.split(","),
        "steps": steps.split(".")
    }

    redis_client.set(name, str(recipe_data))
    print("Recipe added successfully.")

def update_recipe():
    name = input("Enter the name of the recipe to update: ").strip()
    new_name = input("Enter new recipe name (leave blank to keep current): ").strip()
    new_ingredients = input("Enter new ingredients (comma-separated, leave blank to keep current): ").strip()
    new_steps = input("Enter new steps (separated by periods, leave blank to keep current): ").strip()

    recipe_data = redis_client.get(name)
    if recipe_data:
        recipe_data = eval(recipe_data)  # Convert string to dictionary
        if new_name:
            redis_client.delete(name)
            name = new_name
        if new_ingredients:
            recipe_data["ingredients"] = new_ingredients.split(",")
        if new_steps:
            recipe_data["steps"]