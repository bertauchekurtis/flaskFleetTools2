# app.py

from flask import Flask
import fleet
import plane

app = Flask(__name__)

@app.route("/")
def hello_world():
    f = fleet.Fleet()
    p = plane.Plane("787-8 Dreamliner", "Boeing", 235, "Large", 123, 1000, 8700, 800, 650, 30, "Boeing", 245000000)
    pp = plane.Plane("737 MAX 7", "737 MAX", 172, "Small", 43, 12000, 100, 100, 100, 10, "Boeing", 123000000)
    f.addTypeToFleet(p)
    f.getCountOfType(pp)

    return "<p>Hello, World!</p>"