from flask import Flask, render_template, request
from dijkstra import dijkstra
from map_engine import generate_map
from simulator import simulate_ship
from database import init_db, save_route

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/navigate", methods=["POST"])
def navigate():
    start = request.form["start"]
    end = request.form["end"]

    cost, path = dijkstra(start, end)

    save_route(start, end, cost)
    generate_map(path)
    simulate_ship(path)

    return {
        "route": path,
        "distance": cost,
        "map": "naval_map.html"
    }

if __name__ == "__main__":
    app.run(debug=True)