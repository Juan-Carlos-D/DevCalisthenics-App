def calculate_macros(weight, height, age, gender, activity_level, goal, weight_unit='kg', height_unit='cm'):
    # Convert weight to kg if in pounds
    if weight_unit == 'lbs':
        weight = weight * 0.453592

    # Convert height to cm if in inches
    if height_unit == 'inches':
        height = height * 2.54

    # Calculate BMR
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Activity factors
    activity_factors = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    maintenance_calories = bmr * activity_factors[activity_level]

    # Adjust calories based on goal
    if goal == 'maintain':
        calories = maintenance_calories
    elif goal == 'gain_slow':
        calories = maintenance_calories + 250  # Gain ~0.5 lb per week
    elif goal == 'gain_fast':
        calories = maintenance_calories + 500  # Gain ~1 lb per week
    elif goal == 'lose_slow':
        calories = maintenance_calories - 250  # Lose ~0.5 lb per week
    elif goal == 'lose_fast':
        calories = maintenance_calories - 500  # Lose ~1 lb per week

    # Adjust macronutrients based on goal
    if goal in ['maintain', 'gain_slow', 'gain_fast']:
        protein = 2.2 * weight  # grams per kg of body weight
        fats = 0.35 * calories / 9
        carbohydrates = (calories - (protein * 4 + fats * 9)) / 4
    else:  # For weight loss
        protein = 2.2 * weight  # grams per kg of body weight
        fats = 0.25 * calories / 9
        carbohydrates = (calories - (protein * 4 + fats * 9)) / 4

    # Calculate ranges
    def calculate_range(value):
        return round(value * 0.9), round(value * 1.1)
    
    protein_range = calculate_range(protein)
    fats_range = calculate_range(fats)
    carbohydrates_range = calculate_range(carbohydrates)
    
    return {
        'calories': round(calories),
        'protein': round(protein),
        'protein_range': protein_range,
        'carbohydrates': round(carbohydrates),
        'carbohydrates_range': carbohydrates_range,
        'fats': round(fats),
        'fats_range': fats_range
    }
