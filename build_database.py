import os
from datetime import datetime
from config import db
from models import Person, Note

# Data to initialize database with
PEOPLE = [
    {
        "fname": "Gerard",
        "lname": "Milling",
        "notes": [
            ("Cool, a mini-blogging application!"),
            ("This could be useful"),
            ("Well, sort of useful"),
        ],
    },
    {
        "fname": "Janina",
        "lname": "Volkmer",
        "notes": [
            (
                "I'm going to make really profound observations",
            ),
            (
                "Maybe they'll be more obvious than I thought",
            ),
        ],
    },
    {
        "fname": "Henk",
        "lname": "VolMil",
        "notes": [
            ("Has anyone seen my Catnip?"),
            ("I'm really late delivering these!"),
        ],
    },
    {
        "fname": "Pluk",
        "lname": "VolkMil",
        "notes": [
            ("Catnip?? I got it!"),
            ("Need some fishsauce"),
        ],
    },
]

# Delete database file if it exists currently
if os.path.exists('people.db'):
    os.remove('people.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))

    # Add the notes for the person
    for note in person.get("notes"):
        content, timestamp = note
        p.notes.append(
            Note(
                content=content,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )
    db.session.add(p)

db.session.commit()
