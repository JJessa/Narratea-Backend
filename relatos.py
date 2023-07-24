from db import db

#Creamos la tabla con sqlalchemy

class Relatos(db.Model):
    #nombre de tabla
    
    __tablename__= "relatos"
    
    #Conjunto de atributos que van a ser los campos de la tabla
    
    #LLave primaria
    
    id=db.Column(db.Integer, primary_key=True)
    
    #Se le pone el tipo de datos que es entre paréntesis, no son tipo de Python si no que están definidos en SQLAlchemy
    titulo=db.Column(db.String(100))
    relato=db.Column(db.String(1700))

    
    #Método constructor para mapear datos a los campos definidos
    
    def __init__(self, titulo, relato):

        self.titulo=titulo
        self.relato=relato
