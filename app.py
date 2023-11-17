from flask import Flask
from src.controllers.address_controller import address_controller


app = Flask(__name__)
app.register_blueprint(address_controller)


if __name__ == '__main__':
    app.run(debug=True)
