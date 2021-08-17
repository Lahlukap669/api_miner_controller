from flask import Flask, jsonify, request, send_file, send_from_directory
import json
from flask_cors import CORS

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rhcmxoop:oRq6tPr2Gt7DLDD9xXrpZhGHDNm6E8CV@tai.db.elephantsql.com/rhcmxoop"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

@app.route("/", methods=['GET','POST'])
def index():
    if(request.method == 'POST'):
        try:
            ##Called function
            r = db.session.execute("""SELECT * FROM sp_view""").first()
            db.session.commit()
            ##Returned data to program
            return jsonify({'bool': list(r)}), 201
        except Exception as e:
            print(e)
            return jsonify({'bool': False}), 404
    else:
        return jsonify({'status': "not working"})

##STATUS OFF
@app.route("/status_off", methods=['GET','POST'])
def status_off():
    if(request.method == 'POST'):
        try:
            ##Called function
            r = db.session.execute("""SELECT change_value('off');""").scalar()
            db.session.commit()
            ##Returned data to program
            return jsonify({'status': 'off'}), 201
        except Exception as e:
            print(e)
            return jsonify({'bool': False}), 404
    else:
        return jsonify({'status': "not working"})

##STATUS ON
@app.route("/status_on", methods=['GET','POST'])
def status_on():
    if(request.method == 'POST'):
        try:
            ##Called function
            r = db.session.execute("""SELECT change_value('on');""").scalar()
            db.session.commit()
            ##Returned data to program
            return jsonify({'status': 'on'}), 201
        except Exception as e:
            print(e)
            return jsonify({'bool': False}), 404
    else:
        return jsonify({'status': "not working"})

if __name__ == '__main__':
    app.run(debug=True)
