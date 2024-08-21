from flask import Flask, render_template, request, redirect, url_for, abort
from faq import faq_data 
from macronutrients import macronutrients_data
from macroscalc import calculate_macros
from blogs import blogs
from programs import programs
import re

app = Flask(__name__, static_folder='static')

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

@app.route('/blogs')
def blogs_home():
    return render_template('Blogs/blogs_home.html', blogs=blogs)

def process_content(content):
    # Find all occurrences of {{ url_for(...)}}
    matches = re.findall(r"\{\{\s*url_for\([^)]+\)\s*\}\}", content)
    for match in matches:
        # Evaluate the url_for expression
        evaluated_url = eval(match.strip("{{}}"))
        # Replace the url_for expression with the actual URL
        content = content.replace(match, evaluated_url)
    return content

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    blog = next((blog for blog in blogs if blog['id'] == blog_id), None)
    if blog:
        blog['content'] = process_content(blog['content'])
        return render_template('Blogs/blogs.html', blog=blog)
    else:
        return 'Blog not found', 404
    
@app.route('/programs')
def programs_page():
    return render_template('Programs/programs.html', programs=programs)



if __name__ == '__main__':
    app.run(debug=True)