def generate_recommendations(user_id):
    metrics = analyze_health_metrics(user_id)
    
    recommendations = []
    
    if metrics["total_steps"] < 7000:
        recommendations.append("Try to increase your daily step count to at least 7000.")
    
    if metrics["total_exercise_minutes"] < 30:
        recommendations.append("Aim for at least 30 minutes of exercise daily.")
    
    if metrics["total_calories"] > 2000:
        recommendations.append("Your calorie intake is high. Consider adjusting your diet.")
    
    return recommendations

# Example usage:
recommendations = generate_recommendations("user1")
print(recommendations)  # Output: ['Try to increase your daily step count to at least 7000.']
