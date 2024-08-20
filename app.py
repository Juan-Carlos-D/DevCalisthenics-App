from flask import Flask, render_template, request, redirect, url_for
# from faq import faq_data 
# from macronutrients import macronutrients_data
# from macroscalc import calculate_macros
# from exercises import exercises
# from blogs import blogs
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)