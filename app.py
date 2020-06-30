from flask import Flask, render_template
import techCrunch
app = Flask(__name__)


#web scraped dictionary
scraped_dict=techCrunch.get_data()


#homepage route to show the table
@app.route("/")
def home():
    return render_template('homepage.html', scraped_dict=scraped_dict)
