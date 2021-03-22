from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import schedule
import time
import json

app = Flask(__name__, template_folder='templates')

db_host = 'llcunha.com'
db_name = 'llcunh28_seniorPonto'
db_user = 'llcunh28_seniorP'
db_password = 'seniorPonto13'

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_user}:{db_password}@{db_host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Ponto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    includedAt = db.Column(db.DateTime, nullable=False)
    employeeId = db.Column(db.Integer, nullable=False)
    employerId = db.Column(db.Integer, nullable=False)

def serializePonto(ponto):
    return {'includedAt': ponto.includedAt, 'employeeId': ponto.employeeId, 'employerId': ponto.employeeId}

@app.route('/registrarponto', methods=['POST'])
def register():
    try:
        if(not request.form['includedAt']):
            return render_template('error.html', error='Por favor, informe a data do ponto')
        if(not request.form['employeeId']):
            return render_template('error.html', error='Por favor, informe o código de usuário')
        if(not request.form['employerId']):
            return render_template('error.html', error='Por favor, informe o código da empresa')

        ponto = Ponto(includedAt=request.form['includedAt'], employeeId=int(request.form['employeeId']), employerId=int(request.form['employerId']))
        db.session.add(ponto)
        db.session.commit()
        schedule.run_pending()
        return render_template('sucess.html')
    except Exception as e:
        return render_template('error.html', error=e)

@app.route('/')
@app.route('/voltar', methods=['GET'])
def index():
    return render_template('index.html')


def exportToLegacyAndDelete():
    url = 'https://api.mockytonk.com/proxy/ab2198a3-cafd-49d5-8ace-baac64e72222'
    pontos = Ponto.query.all()
    for ponto in pontos:
        x = requests.post(url, data = serializePonto(ponto))
        if(x.ok):
            db.session.delete(ponto)
            db.session.commit()

schedule.every(3).seconds.do(exportToLegacyAndDelete)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)