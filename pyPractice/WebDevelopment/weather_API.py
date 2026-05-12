from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
	"new_york": {"temperature": 25, "condition": "Sunny"},
	"london": {"temperature": 18, "condition": "Cloudy"},
	"tokyo": {"temperature": 30, "condition": "Rainy"},
	"sydney": {"temperature": 22, "condition": "Windy"},
	"paris": {"temperature": 20, "condition": "Foggy"},
	"berlin": {"temperature": 15, "condition": "Snowy"},
	"dublin": {"temperature": 17, "condition": "Drizzle"}
}

@app.route('/')
def home():
	return jsonify({"message":"Welcome to the Weather App!"})

@app.route('/weather', methods=['GET'])
def get_all_weather():
	return jsonify(weather_data)

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
	city = city.lower()
	try:
		return jsonify(weather_data[city])
	except Exception as e:
		return jsonify({"error": f"{e}"})
	
@app.route('/weather', methods=['POST'])
def add_city_weather():
	data = request.json
	city = data.get('city','').lower()
	temperature = data.get('temperature')
	condition = data.get('condition')

	if not city or temperature is None or not condition:
		return jsonify({"error": "City, temperature, and condition are required."}), 400

	weather_data[city] = {"temperature": temperature, "condition": condition}
	return jsonify({"message": f"Weather data added for {city}."})

if __name__ == "__main__":
	app.run(debug=True)