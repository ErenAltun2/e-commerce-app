from flask import Flask, render_template
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metric definition
requests_total = Counter('requests_total', 'Total HTTP requests')

# Ürünler ve sepet
products = [{'id': 1, 'name': 'Telefon', 'price': 1000}, {'id': 2, 'name': 'Laptop', 'price': 5000}]
cart = []

# Ana sayfa
@app.route('/')
def home():
    requests_total.inc()  # Her istek geldiğinde sayacı artır
    return render_template('index.html', products=products)

# Sepete ürün ekleme
@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        return f"{product['name']} sepete eklendi!"
    return "Ürün bulunamadı."

# Prometheus için metrikler
@app.route('/metrics')
def metrics():
    return generate_latest()  # Prometheus formatında metrikleri döndür

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
