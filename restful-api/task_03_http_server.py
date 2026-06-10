#!/usr/bin/python3
"""
Petit serveur HTTP simple avec http.server.
Il répond selon l'URL demandée.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Classe qui gère les requêtes HTTP GET."""

    def do_GET(self):
        """Traite les requêtes GET selon le chemin demandé."""

        # Cas 1 : page d'accueil
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Cas 2 : endpoint /data
        elif self.path == "/data":
            # Données à envoyer au format JSON
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            # Conversion du dictionnaire Python en chaîne JSON
            response = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode())

        # Cas 3 : endpoint /status
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Cas 4 : endpoint /info
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            response = json.dumps(info)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode())

        # Cas 5 : endpoint inconnu
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Démarre le serveur sur le port 8000."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)

    print(f"Serving on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
