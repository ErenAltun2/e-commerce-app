from flask import Flask, render_template, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

requests_total = Counter('requests_total', 'Total HTTP requests')

products = [{'id': 1, 'name': 'Telefon', 'price': 1000}, {'id': 2, 'name': 'Laptop', 'price': 5000}]
cart = []

@app.route('/')
def home():
    requests_total.inc()
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        return f"{product['name']} sepete eklendi!"
    return "Ürün bulunamadı."

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)