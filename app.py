from flask import Flask
from flask_cors import CORS

from services.ping import service_ping

app = Flask(__name__)
app.register_blueprint(service_ping)
CORS(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
