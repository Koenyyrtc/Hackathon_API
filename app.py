from flask import Flask, jsonify, request
import random
import json
import datetime
from currency import convert_currency
from password import generate_password
from user import random_user

app = Flask(__name__)

# Load data files
with open('data/quotes.json') as f:
    quotes = json.load(f)

with open('data/facts.json') as f:
    facts = json.load(f)


# 1. Random Quote
@app.route('/random-quote', methods=['GET'])
def random_quote():
    return jsonify({'quote': random.choice(quotes)})

# 2. Random Image
@app.route('/random-image', methods=['GET'])
def random_image():
    return jsonify({'image_url': f'/static/{random.randint(1, 100)}.jpg'})

# 3. Random Fact
@app.route('/random-fact', methods=['GET'])
def random_fact():
    return jsonify({'fact': random.choice(facts)})

# 5. Random User Profile
@app.route('/random-user', methods=['GET'])
def random_user_profile():
    return jsonify(random_user())

# 6. Currency Conversion
@app.route('/currency-convert', methods=['GET'])
def currency_convert():
    amount = float(request.args.get('amount'))
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    converted = convert_currency(amount, from_currency, to_currency)
    return jsonify({'converted_amount': converted})

# 7. Random Color
@app.route('/random-colour', methods=['GET'])
def random_color():
    return jsonify({'colour': f'#{random.randint(0, 0xFFFFFF):06x}'})

# 8. Random Advice
@app.route('/random-advice', methods=['GET'])
def random_advice():
    advices = ["Always be yourself.", "Stay positive.", "Never give up.", "Work hard."]
    return jsonify({'advice': random.choice(advices)})

# 10. Random Activity
@app.route('/random-activity', methods=['GET'])
def random_activity():
    activities = ["Go for a run", "Read a book", "Learn a new skill", "Watch a movie"]
    return jsonify({'activity': random.choice(activities)})

# 11. Random Location (City/Country)
@app.route('/random-location', methods=['GET'])
def random_location():
    locations = ["New York", "Tokyo", "Paris", "London", "Hong Kong"]
    return jsonify({'location': random.choice(locations)})

# 12. Random Number
@app.route('/random-number', methods=['GET'])
def random_number():
    min_val = int(request.args.get('min', 0))
    max_val = int(request.args.get('max', 1000))
    return jsonify({'random_number': random.randint(min_val, max_val)})

# 13. Random Password Generator
@app.route('/random-password', methods=['GET'])
def random_password():
    length = int(request.args.get('length', 8))
    password = generate_password(length)
    return jsonify({'password': password})

# 14. Random Emoji
@app.route('/random-emoji', methods=['GET'])
def random_emoji():
    emojis = ["😊", "😂", "👍", "🎉", "💡"]
    return jsonify({'emoji': random.choice(emojis)})

# 15. Current Date and Time
@app.route('/current-datetime', methods=['GET'])
def current_datetime():
    current_time = datetime.datetime.now().isoformat()
    return jsonify({'datetime': current_time})

if __name__ == '__main__':
    app.run(debug=True)

