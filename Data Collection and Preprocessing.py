# Example of in-memory data collection for users' activities and diet
users_data = {}

def log_activity(user_id, steps, exercise_minutes):
    if user_id not in users_data:
        users_data[user_id] = {"activities": [], "diet": []}
    users_data[user_id]["activities"].append({"steps": steps, "exercise_minutes": exercise_minutes})

def log_diet(user_id, calories, meal_type):
    if user_id not in users_data:
        users_data[user_id] = {"activities": [], "diet": []}
    users_data[user_id]["diet"].append({"calories": calories, "meal_type": meal_type})

# Example logging data
log_activity("user1", 5000, 30)
log_diet("user1", 600, "breakfast")
