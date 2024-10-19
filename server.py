
from flask import Flask, jsonify
from upload import packIT
from scrape_main import MAIN_SCRAPER

# Initialize Flask app
app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/events', methods=['GET'])
def send_data():
    # Sample data to be sent
    data = packIT(MAIN_SCRAPER('https://umdearborn.campuslabs.com/engage/events'))
     
    return jsonify(data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)