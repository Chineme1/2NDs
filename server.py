import os
from flask import Flask, jsonify
from upload import packIT
from scrape_main import MAIN_SCRAPER

# Initialize Flask app
app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/', methods=['GET'])
def send_data():
    # Sample data to be sent
    print('req')
    data = packIT(MAIN_SCRAPER('https://umdearborn.campuslabs.com/engage/events'))
    print('data')
    return jsonify(data)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
