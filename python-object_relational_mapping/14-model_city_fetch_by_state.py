#!/usr/bin/python3
"""
Ce module utilise SQLAlchemy pour lister tous les objets State
contenant la lettre 'a' presents dans la base de donnees.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id).all()
    )

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
