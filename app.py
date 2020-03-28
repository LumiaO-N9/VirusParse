from flask import Flask, render_template, jsonify
from db.totalStaticTable import engine, TotalStatic
from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


@app.route('/test')
def testStatic():
    return render_template('virusMap.html')


@app.route('/getMapData')
def getMapData():
    session = DBSession()
    totalStatics = session.query(TotalStatic).all()
    totalStaticsList = []
    for totalStatic in totalStatics:
        dictTemp = {}
        dictTemp["name"] = totalStatic.region
        dictTemp["value"] = int(totalStatic.total_confirm)
        totalStaticsList.append(dictTemp)
    print(totalStaticsList)
    return jsonify(totalStaticsList)
