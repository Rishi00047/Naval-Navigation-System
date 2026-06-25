import time

def simulate_ship(path):
    print("\n🚢 Ship Simulation Started...\n")

    for i, port in enumerate(path):
        print(f"➡ Moving to {port}")
        time.sleep(1)  # simulation delay

    print("\n✅ Ship reached destination safely.")