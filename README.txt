NAVAL NAVIGATION SYSTEM
-----------------------

PROJECT DESCRIPTION:
This project is a Python-based Naval Navigation System that simulates sea route planning between ports using graph algorithms. It calculates the shortest route using Dijkstra’s algorithm and visualizes the route on an interactive map.

FEATURES:
- Shortest path calculation between ports
- Interactive map visualization using Folium
- Ship route simulation
- Restricted zone display
- Route history storage using SQLite
- Web interface using Flask

HOW TO RUN:
1. Install required libraries:
   pip install flask folium requests

2. Run the application:
   python app.py

3. Open browser and go to:
   http://127.0.0.1:5000/

PROJECT STRUCTURE:
- app.py → Main Flask application
- graph.py → Ports and connections
- dijkstra.py → Shortest path algorithm
- map_engine.py → Map generation
- simulator.py → Ship movement simulation
- database.py → Route storage system

OUTPUT:
- Interactive naval route map (HTML file)
- Route distance and travel time
- Simulated ship movement