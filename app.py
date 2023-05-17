from flask import render_template
import config
from models import Person

# Connect API config file to flask app - i.e. adding module to program
app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

# connect url route to home - creates basic web server and has it respond with home.html 
@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)