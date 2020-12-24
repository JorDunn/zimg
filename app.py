from flask import Flask
from routes.routes import main

app = Flask(__name__, template_folder='views')
app.debug = True
app.env = 'Development'

app.register_blueprint(main)

app.run('0.0.0.0', 3000)
