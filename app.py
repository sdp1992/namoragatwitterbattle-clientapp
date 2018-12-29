from flask import Flask,jsonify,request
from flask import render_template
import ast

app = Flask(__name__)

labels = [1,2,3,4,5,6,7,8,9,10]
namo_values = [1,2,3,4,5,6,7,8,9,10]
raga_values = [1,2,3,4,5,6,7,8,9,10]


@app.route("/")
def chart():
    global labels, namo_values, raga_values
    labels = [1,2,3,4,5,6,7,8,9,10]
    namo_values = [1,2,3,4,5,6,7,8,9,10]
    raga_values = [1,2,3,4,5,6,7,8,9,10]
    return render_template('index.html', labels=labels, namo_values=namo_values, raga_values=raga_values)


@app.route('/refreshData')
def refresh_graph_data():
    global labels, namo_values, raga_values
    print("labels now: " + str(labels))
    print("Namo data now: " + str(namo_values))
    print("Raga data now: " + str(raga_values))
    return jsonify(sLabel=labels, sNamoData=namo_values, sRagaData = raga_values)


@app.route('/updateData', methods=['POST'])
def update_data_post():
    global labels, namo_values, raga_values
    if not request.form or 'namo_data' not in request.form:
        return "Error",400

    labels = ast.literal_eval(request.form['label'])
    namo_values.pop(0)
    namo_values.append(ast.literal_eval(request.form['namo_data'])[0])
    raga_values.pop(0)
    raga_values.append(ast.literal_eval(request.form['raga_data'])[0])
    print("labels received: " + str(labels))
    print("Namo data received: " + str(namo_values))
    print("Namo data received: " + str(raga_values))
    return "success",201


if __name__ == "__main__":
    app.run()

