from flask import Flask, jsonify, request
from flask_cors import CORS
from db import db
from relatos import Relatos

class Program:
    
    def __init__(self):
        
        self.app = Flask(__name__)
        CORS(self.app)
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///relatos.sqlite3"
        db.init_app(self.app)
        
        self.app.add_url_rule("/api/relatos", view_func=self.get_relatos, methods=["GET"])
        self.app.add_url_rule("/api/relatos", view_func=self.agregar_relato, methods=["POST"])
        self.app.add_url_rule("/api/relatos/<int:relato_id>", view_func=self.eliminar_relato, methods=["DELETE"])
        self.app.add_url_rule("/api/relatos/<int:relato_id>", view_func=self.actualizar_relato, methods=["PUT"])
        
        
        with self.app.app_context():
            db.create_all()
        
        self.app.run(debug=True)
    
    def get_relatos(self):
        relatos = Relatos.query.all()
        relatos_data = [
            {"id": relato.id, "titulo": relato.titulo, "relato": relato.relato}
            for relato in relatos
        ]
        return jsonify(relatos=relatos_data)
    
    def agregar_relato(self):
        titulo = request.json.get('titulo')
        relato = request.json.get('relato')
        
        nuevo_relato = Relatos(titulo=titulo, relato=relato)
        db.session.add(nuevo_relato)
        db.session.commit()
        
        return jsonify(message="Relato agregado exitosamente")
    
    def eliminar_relato(self, relato_id):

        relato = Relatos.query.get(relato_id)
        
        if relato:
            db.session.delete(relato)
            db.session.commit()
            return jsonify(message="Relato eliminado exitosamente")
        
        return jsonify(error="Relato no encontrado"), 404
    
    def actualizar_relato(self, relato_id):
        relato = Relatos.query.get(relato_id)
        
        if relato:
            titulo = request.json.get('titulo')
            relato_nuevo = request.json.get('relato')
            
            relato.titulo = titulo
            relato.relato = relato_nuevo
            db.session.commit()
            
            return jsonify(message="Relato actualizado exitosamente")
        
        return jsonify(error="Relato no encontrado"), 404

myProgram = Program()
