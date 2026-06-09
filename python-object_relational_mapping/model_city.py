#!/usr/bin/python3
"""
Ce module definit la classe City pour le mapping
de la table 'cities' avec SQLAlchemy.
"""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
    Classe City qui lie le modele Python a la table MySQL 'cities'.

    Attributs:
        id (int): L'identifiant unique de la ville (Cle primaire).
        name (str): Le nom de la ville (Max 128 caracteres, non nul).
        state_id (int): L'ID de l'etat associe (Cle etrangere vers states.id).
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
