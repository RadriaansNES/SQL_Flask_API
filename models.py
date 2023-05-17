from datetime import datetime
from config import db, ma # import database, marsh
from marshmallow_sqlalchemy import fields

# define SQLalch model for note object
class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

# define note schme to deserialize notes
class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True

# defining persons class, where inheritance gives access to database/tables
class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    # add relational to collection of notes
    notes = db.relationship(
        Note,
        backref="person",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Note.timestamp)"
    )
# create personschema class to define how python object will be converted into JSON
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session
        # explicitly dictate schema to include relationships
        include_relationships = True
    notes = fields.Nested(NoteSchema, many=True)

note_schema = NoteSchema()
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)