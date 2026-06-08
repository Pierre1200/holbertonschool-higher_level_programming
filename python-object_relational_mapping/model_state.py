#!/usr/bin/python3
"""
Ce module definit la classe State et l'instance Base
pour le mapping de la table 'states' avec SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Classe State qui mappe la table 'states' de la base de données.
    Attributs:
        id (int): Identifiant unique de l'état (clé primaire).
        name (str): Nom de l'état (non nul).
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
