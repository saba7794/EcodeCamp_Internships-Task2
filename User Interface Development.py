from flask import Flask, request, render_template_string

app = Flask(__name__)

# In-memory data structure for storing activity and diet logs
users_data = {}

# Simple HTML forms for activity and diet logging
HTML_FORM = """
<!doctype html>
<html>
    <head><title>Health Tracker</title></head>
    <body>
        <h1>Log Your Activity</h1>
        <form method="post" action="/log_activity">
            <label for="steps">Steps:</label><br>
            <input type="number" id="steps" name="steps"><br><br>
            <label for="exercise_minutes">Exercise Minutes:</label><br>
            <input type="number" id="exercise_minutes" name="exercise_minutes"><br><br>
            <input type="submit" value="Log Activity">
        </form>
        <h1>Log Your Diet</h1>
        <form method="post" action="/log_diet">
            <label for="calories">Calories:</label><br>
            <input type="number" id="calories" name="calories"><br><br>
            <label for="meal_type">Meal Type:</label><br>
            <input type="text" id="meal_type" name="meal_type"><br><br>
            <input type="submit" value="Log Diet">
        </form>
        <h1>Get Recommendations</h1>
        <form method="get" action="/get_recommendations">
            <input type="submit" value="Get Recommendations">
        </form>
    </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_FORM)

@app.route("/log_activity", methods=["POST"])
def log_activity():
    steps = request.form.get("steps")
    exercise_minutes = request.form.get("exercise_minutes")
    user_id = "user1"  # Placeholder for simplicity
    if user_id not in users_data:
        users_data[user_id] = {"activities": [], "diet": []}
    users_data[user_id]["activities"].append({"steps": steps, "exercise_minutes": exercise_minutes})
    return "Activity logged successfully! <br><a href='/'>Go Back</a>"

@app.route("/log_diet", methods=["POST"])
def log_diet():
    calories = request.form.get("calories")
    meal_type = request.form.get("meal_type")
    user_id = "user1"  # Placeholder for simplicity
    if user_id not in users_data:
        users_data[user_id] = {"activities": [], "diet": []}
    users_data[user_id]["diet"].append({"calories": calories, "meal_type": meal_type})
    return "Diet logged successfully! <br><a href='/'>Go Back</a>"

# Health metrics analysis
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

# Generate personalized recommendations
def generate_recommendations(user_id):
    metrics = analyze_health_metrics(user_id)
    
    if not metrics:
        return ["No data available. Please log your activities and diet first."]
    
    recommendations = []
    
    if metrics["total_steps"] < 7000:
        recommendations.append("Try to increase your daily step count to at least 7000.")
    
    if metrics["total_exercise_minutes"] < 30:
        recommendations.append("Aim for at least 30 minutes of exercise daily.")
    
    if metrics["total_calories"] > 2000:
        recommendations.append("Your calorie intake is high. Consider adjusting your diet.")
    
    return recommendations

@app.route("/get_recommendations", methods=["GET"])
def get_recommendations():
    user_id = "user1"  # Placeholder
    recommendations = generate_recommendations(user_id)
    
    # Render recommendations using render_template_string
    recommendations_html = ''.join(f"<li>{r}</li>" for r in recommendations)
    return render_template_string(f"""
    <!doctype html>
    <html>
        <head><title>Recommendations</title></head>
        <body>
            <h2>Your Recommendations:</h2>
            <ul>{recommendations_html}</ul>
            <a href='/'>Go Back</a>
        </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
