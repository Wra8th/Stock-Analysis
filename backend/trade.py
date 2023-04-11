from bsedata.bse import BSE
from flask import Flask, jsonify, request
import json
from flask_cors import CORS

b = BSE();
# print(b.getQuote('534976'));

# Initializing flask app
app = Flask(__name__)
  
CORS(app)

# Route for seeing a data
@app.route('/data')
@app.route('/submit', methods=['POST'])

def submit():
    if request.method == 'POST':
        data = request.get_json()
        print(data['quote'])
        quoteDicted = b.getQuote(data['quote'])
        return quoteDicted
    else:
        quoteDict = b.getQuote('534976')
        convertedJson = json.dumps(quoteDict, indent = 3)
        return jsonify(
            quoteDict
        )
    

# Running app
if __name__ == '__main__':
    app.run(debug=True)