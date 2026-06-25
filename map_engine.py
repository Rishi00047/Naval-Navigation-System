import folium
from graph import ports

def generate_map(path):
    m = folium.Map(location=ports[path[0]], zoom_start=5)

    # Ports
    for name, coord in ports.items():
        folium.Marker(coord, tooltip=name).add_to(m)

    # Route line
    route = [ports[p] for p in path]

    folium.PolyLine(route, color="red", weight=4).add_to(m)

    # Ship animation (simple marker movement)
    for i, point in enumerate(route):
        folium.Marker(
            point,
            popup=f"Step {i+1}",
            icon=folium.Icon(color="blue", icon="ship")
        ).add_to(m)

    m.save("naval_map.html")