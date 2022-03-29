from flask import Flask, jsonify, render_template, Blueprint
import random
from flask_cors import CORS


app = Flask(__name__, static_folder='static', static_url_path='/frontdesk/static')
CORS(app)
app.config["APPLICATION_ROOT"] = '/frontdesk'
bp = Blueprint('bp', __name__,template_folder='templates')
app.register_blueprint(bp, url_prefix='/frontdesk')

@bp.route('/')
@app.route('/frontdesk')
@app.route('/frontdesk/')
def index():
    num = random.randrange(100,1000)
    return render_template("index.html", num=num)
  

if __name__ == '__main__':
    app.run(host="0.0.0.0", ssl_context=("cert.pem", "key.pem"), debug=True, port=8000)
