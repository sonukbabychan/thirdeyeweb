from flask import *
from public import public
from caretaker import caretaker
from admin import admin

app=Flask(__name__)
app.secret_key="blindapp"

app.register_blueprint(public)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(caretaker, url_prefix='/caretaker')
# app.register_blueprint(api, url_prefix='/api')
app.run(debug=True, port=5005)