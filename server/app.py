from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Customer, Hardware, Manufacturer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Customer/Hardware/Manufacturer API"

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    customer_list = []
    for customer in customers:
        customer_data = {
            'id': customer.id,
            'firstname': customer.firstname,
            'lastname': customer.lastname,
            'email': customer.email,
            'phone': customer.phone
        }
        customer_list.append(customer_data)
    return jsonify(customers=customer_list)


@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    customer_data = {
        'id': customer.id,
        'firstname': customer.firstname,
        'lastname': customer.lastname,
        'email': customer.email,
        'phone': customer.phone
    }
    return jsonify(customer=customer_data)

@app.route("/addcustomers", methods = ["POST"])
def post_customer():
    data = request.get_json()
    new_customer = Customer(
        firstname = data["firstname"],
        lastname = data["lastname"],
        email = data["email"],
        phone = data["phone"],
        password = data["password"]
    )
    db.session.add(new_customer)
    db.session.commit()
    return make_response(jsonify({"message":"Customer added successfully"}))






# Hardware routes

@app.route('/hardware', methods=['GET'])
def get_hardware():
    hardware = Hardware.query.all()
    hardware_list = []
    for item in hardware:
        hardware_data = {
            'id': item.id,
            'customer_id': item.customer_id,
            'manufacturer_id': item.manufacturer_id,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'category': item.category
        }
        hardware_list.append(hardware_data)
    return jsonify(hardware=hardware_list)

@app.route('/hardware/<int:hardware_id>', methods=['GET'])
def get_hardware_item(hardware_id):
    item = Hardware.query.get_or_404(hardware_id)
    hardware_data = {
        'id': item.id,
        'customer_id': item.customer_id,
        'manufacturer_id': item.manufacturer_id,
        'name': item.name,
        'description': item.description,
        'price': item.price,
        'category': item.category
    }
    return jsonify(hardware=hardware_data)

@app.route("/addhardwares", methods = ["POST"])
def post_hardware():
    data = request.get_json()
    new_hardware = Hardware(
        customer_id = data["customer_id"],
        manufacturer_id = data["manufacturer_id"],
        name = data["name"],
        description = data["description"],
        price = data["price"],
        category=data["category"],
    )
    db.session.add(new_hardware)
    db.session.commit()
    return make_response(jsonify({"message":"Hardware added successfully"}))

# Manufacturer routes

@app.route('/manufacturers', methods=['GET'])
def get_manufacturers():
    manufacturers = Manufacturer.query.all()
    manufacturer_list = []
    for manufacturer in manufacturers:
        manufacturer_data = {
            'id': manufacturer.id,
            'firstname': manufacturer.firstname,
            'lastname': manufacturer.lastname,
            'email': manufacturer.email,
            'phone': manufacturer.phone
        }
        manufacturer_list.append(manufacturer_data)
    return jsonify(manufacturers=manufacturer_list)

@app.route('/manufacturers/<int:manufacturer_id>', methods=['GET'])
def get_manufacturer(manufacturer_id):
    manufacturer = Manufacturer.query.get_or_404(manufacturer_id)
    manufacturer_data = {
        'id': manufacturer.id,
        'firstname': manufacturer.firstname,
        'lastname': manufacturer.lastname,
        'email': manufacturer.email,
        'phone': manufacturer.phone
    }
    return jsonify(manufacturer=manufacturer_data)


@app.route("/addmanufacturer", methods = ["POST"])
def post_manufacturer():
    data = request.get_json()
    new_manufacturer = Manufacturer(
        firstname = data["firstname"],
        lastname = data["lastname"],
        email = data["email"],
        phone = data["phone"],
        password = data["password"]
    )
    db.session.add(new_manufacturer)
    db.session.commit()
    return make_response(jsonify({"message":"Manufacturer added successfully"}))


if __name__ == '__main__':
    app.run(port=5555)