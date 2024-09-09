def analyze_health_metrics(user_id):
    if user_id not in users_data:
        return None
    
    activities = users_data[user_id]["activities"]
    diet = users_data[user_id]["diet"]
    
    total_steps = sum(int(activity["steps"]) for activity in activities)
    total_exercise_minutes = sum(int(activity["exercise_minutes"]) for activity in activities)
    total_calories = sum(int(meal["calories"]) for meal in diet)
    
    return {
        "total_steps": total_steps,
        "total_exercise_minutes": total_exercise_minutes,
        "total_calories": total_calories
    }

# Example usage:
metrics = analyze_health_metrics("user1")
print(metrics)  # Output: {'total_steps': 5000, 'total_exercise_minutes': 30, 'total_calories': 600}
