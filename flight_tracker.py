from pyflightdata import FlightData

# Initialize FlightData object
f = FlightData()

# Function to get last known location of a flight
def get_flight_info(tail_number):
    try:
        flight_history = f.get_history_by_tail_number(tail_number)
        if flight_history and len(flight_history) > 0:
            last_flight = flight_history[0]  # Get the most recent flight
            
            # Extract departure and arrival safely
            departure = last_flight.get("airport", {}).get("origin", {}).get("name", "Unknown")
            arrival = last_flight.get("airport", {}).get("destination", {}).get("name", "Unknown")
            
            # Handle cases where 'arrival' is missing
            if not arrival or arrival == "Unknown":
                arrival = last_flight.get("airport", {}).get("destination", {}).get("code", "Unknown")  # Use airport code if name is missing
            
            aircraft = last_flight.get("aircraft", {}).get("model", "Unknown")
            date = last_flight.get("time", {}).get("scheduled", {}).get("departure", "Unknown")

            return {
                "Tail Number": tail_number,
                "Departure": departure,
                "Arrival": arrival,
                "Aircraft": aircraft,
                "Date": date
            }
        else:
            return {"Tail Number": tail_number, "Error": "No flight history found"}
    except Exception as e:
        return {"Tail Number": tail_number, "Error": str(e)}

# List of tail numbers (Tom Cruise, Taylor Swift, and one additional)
tail_numbers = ["N350XX", "N621MM", "N628TS"]  # N628TS is Elon Musk's jet

# Fetch and display flight data
for tail in tail_numbers:
    flight_info = get_flight_info(tail)
    print(f"\nFlight Data for {flight_info['Tail Number']}:")
    
    if "Error" in flight_info:
        print(f"Error: {flight_info['Error']}")
    else:
        print(f"Departure: {flight_info.get('Departure', 'Unknown')}")
        print(f"Arrival: {flight_info.get('Arrival', 'Unknown')}")
        print(f"Aircraft: {flight_info.get('Aircraft', 'Unknown')}")
        print(f"Date: {flight_info.get('Date', 'Unknown')}")
