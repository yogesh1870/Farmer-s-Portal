from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


carts = {}
agri_prices = {
    "Rice": 35.0,
    "Wheat": 25.0,
    "Barley": 40.0,
    "Maize": 30.0,
    "Sugarcane": 300.0,
    "Cotton": 50.0,
    "Tea": 200.0,
    "Coffee": 150.0,
    "Soybean": 70.0,
    "Mustard": 45.0,
    "Groundnut": 100.0,
    "Pulses": 70.0,
    "Chillies": 90.0,
    "Onion": 40.0,
    "Potato": 30.0,
    "Tomato": 25.0,
    "Carrot": 50.0,
    "Cabbage": 20.0,
    "Spinach": 15.0,
    "Cauliflower": 25.0
}



@app.route('/')
def index():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html',prices=agri_prices,date=current_date)


@app.route('/admin')
def admin():
    return render_template('admin.html',prices=agri_prices)


@app.route('/update', methods=['POST'])
def update():
    # Update the price of the item based on user input
    item = request.form['item']
    new_price = request.form['price']

    if item in agri_prices:
        agri_prices[item] = float(new_price)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)



