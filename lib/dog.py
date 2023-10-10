# lib/dog.py

from lib.models import Dog

def create_table():
    # Create the database table if it doesn't exist
    Base.metadata.create_all(engine)

def create_dog(name, breed):
    # Create a new dog record in the database
    new_dog = Dog(name=name, breed=breed)
    session.add(new_dog)
    session.commit()

def read_dog(name):
    # Retrieve a dog record by its name
    return session.query(Dog).filter_by(name=name).first()

def update_dog(name, new_name, new_breed):
    # Update a dog's name and breed
    dog = session.query(Dog).filter_by(name=name).first()
    if dog:
        dog.name = new_name
        dog.breed = new_breed
        session.commit()

def delete_dog(name):
    # Delete a dog record by its name
    dog = session.query(Dog).filter_by(name=name).first()
    if dog:
        session.delete(dog)
        session.commit()
