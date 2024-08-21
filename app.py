from flask import Flask, render_template, request, redirect, url_for
from faq import faq_data 
from macronutrients import macronutrients_data
from macroscalc import calculate_macros
# from exercises import exercises
# from blogs import blogs
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/nutrition')
def macronutrients():
    return render_template('Nutrition/macronutrients.html', macronutrients=macronutrients_data)   
    
@app.route('/macrocalculator', methods=['GET', 'POST'])
def macrocalculator():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']
        activity_level = request.form['activity_level']
        goal = request.form['goal']
        weight_unit = request.form['weight_unit']
        height_unit = request.form['height_unit']

        macros = calculate_macros(weight, height, age, gender, activity_level, goal, weight_unit, height_unit)
        return render_template('Nutrition/macroscalc.html', macros=macros, weight=weight, height=height, age=age, gender=gender, activity_level=activity_level, goal=goal, weight_unit=weight_unit, height_unit=height_unit)

    return render_template('Nutrition/macroscalc.html')

@app.route('/faq')
def faq():
    return render_template('FAQ/FAQ.html', faq_data=faq_data)


if __name__ == '__main__':
    app.run(debug=True)