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
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))
    session.close()
