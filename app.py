from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store item details
d = {}


# Route to display the form for adding items

@app.route('/add_data')
def index():
    return render_template('get_input.html')


# Route to display the price list
@app.route('/')
def price_list():
    return render_template('price_list.html', d=d)


# Route to handle the form submission and add item details to the dictionary
@app.route('/add', methods=['POST'])
def input_price():
    if request.method == 'POST':
        # Retrieve data from the form
        id_no = request.form['item_no']
        name = request.form['item_name']
        price = request.form['price']

        # Store item in the dictionary with item_no as key
        d[id_no] = {'name': name, 'price': price}

        # Redirect to price list page after adding item
        return redirect(url_for('price_list'))

    return redirect(url_for('index'))


@app.route('/remove/<id>')
def delete(id):
    if id in d:
        del d[id]
        return redirect(url_for('price_list'))




if __name__ == '__main__':
    app.run(debug=True)



