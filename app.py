from flask import Flask, request, render_template_string

app = Flask(__name__)

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
    </body>
</html>
"""

# In-memory data structure for storing activity and diet logs
users_data = {}

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
    return "Activity logged successfully!"

@app.route("/log_diet", methods=["POST"])
def log_diet():
    calories = request.form.get("calories")
    meal_type = request.form.get("meal_type")
    user_id = "user1"  # Placeholder for simplicity
    if user_id not in users_data:
        users_data[user_id] = {"activities": [], "diet": []}
    users_data[user_id]["diet"].append({"calories": calories, "meal_type": meal_type})
    return "Diet logged successfully!"

if __name__ == "__main__":
    app.run(debug=True)
