from flask import Flask, jsonify
from scrape_main import MAIN_SCRAPER

# Initialize Flask app
app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/events', methods=['GET'])
def send_data():
    # Sample data to be sent
    data = {
        'title': ["a","b","c","d"],
        'location': 'UC 1223',
        'start time': 'Software Developer',
        'end time': 'New York'
        
    }
     
    return jsonify(data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)