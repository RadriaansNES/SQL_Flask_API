import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Create variable basedir pointing to the  directory that the program is running in
basedir = pathlib.Path(__file__).parent.resolve()
# create connexion app instance and gives it path directory
connex_app = connexion.App(__name__, specification_dir=basedir)

# initliaze flask instance
app = connex_app.app
# tell sqlAlchemy to use SQLite as database and subsequent file
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#init SQLAlch, marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)