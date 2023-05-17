from flask import render_template
import connexion

# Connect API config file to flask app - i.e. adding module to program
app = connexion.App(__name__, specification_dir="./")
# read config file
app.add_api("swagger.yml")

# connect url route to home - creates basic web server and has it respond with home.html 
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)