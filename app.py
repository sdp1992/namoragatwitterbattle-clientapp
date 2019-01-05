from flask import Flask,jsonify,request
from flask import render_template
import ast

app = Flask(__name__)


def initialize_value(return_params):
        count_values = []
        for i in range(360):
            count_values.append(0)
        labels_values = []
        j = 6
        for i in range(360):
            if i in [0,60,120,180,240,300]:
                labels_values.append("-" + str(10*j) + " Min")
                j = j-1
            else:
                labels_values.append("")
        if return_params == "labels":
            return labels_values
        else:
            return count_values


labels1 = initialize_value("labels")
labels2 = initialize_value("labels")

namo_count = initialize_value("count")
raga_count = initialize_value("count")

namo_positive = initialize_value("count")
raga_positive = initialize_value("count")

namo_negative = initialize_value("count")
raga_negative = initialize_value("count")


@app.route("/")
def chart():
    global labels1, labels2, namo_count, raga_count, namo_positive, namo_negative, raga_positive, raga_negative

    return render_template('index.html', labels1=labels1, labels2=labels2,
                           namo_count=namo_count, raga_count=raga_count,
                           namo_positive = namo_positive, raga_positive = raga_positive,
                           namo_negative = namo_negative, raga_negative = raga_negative)


@app.route('/refreshData')
def refresh_graph_data():
    global labels1, labels2, namo_count, raga_count, namo_positive, namo_negative, raga_positive, raga_negative

    # print("labels1 now: " + str(labels1))
    # print("labels2 now: " + str(labels2))
    # print("Namo count now: " + str(namo_count))
    # print("Raga count now: " + str(raga_count))
    # print("Namo positive count now: " + str(namo_positive))
    # print("Namo negative count now: " + str(namo_negative))
    # print("Raga positive count now: " + str(raga_positive))
    # print("Raga negative count now: " + str(raga_negative))

    return jsonify(sLabel1=labels1, sLabel2=labels2, sNamoData=namo_count, sRagaData=raga_count,
                   sNamoPositive=namo_positive, sNamoNegative=namo_negative,
                   sRagaPositive=raga_positive, sRagaNegative=raga_negative)


@app.route('/updateData', methods=['POST'])
def update_data_post():
    global labels1, namo_count, raga_count
    if not request.form or 'namo_count' not in request.form:
        return "Error",400

    #labels1 = ast.literal_eval(request.form['label'])

    namo_count.pop(0)
    namo_count.append(ast.literal_eval(request.form['namo_count'])[0])

    raga_count.pop(0)
    raga_count.append(ast.literal_eval(request.form['raga_count'])[0])

    #print("labels received: " + str(labels1))
    # print("Namo data received: " + str(namo_count))
    # print("Namo data received: " + str(raga_count))

    return "success",201


@app.route('/updateSentimentData', methods=['POST'])
def update_data_post_sentiment():
    global labels2, namo_positive, namo_negative, raga_positive, raga_negative
    if not request.form or 'namo_positive' not in request.form:
        return "Error",400

    #labels2 = ast.literal_eval(request.form['label'])

    namo_positive.pop(0)
    namo_positive.append(ast.literal_eval(request.form['namo_positive'])[0])

    namo_negative.pop(0)
    namo_negative.append(ast.literal_eval(request.form['namo_negative'])[0])

    raga_positive.pop(0)
    raga_positive.append(ast.literal_eval(request.form['raga_positive'])[0])

    raga_negative.pop(0)
    raga_negative.append(ast.literal_eval(request.form['raga_negative'])[0])

    # print("labels received: " + str(labels2))
    # print("Namo positive count received: " + str(namo_positive))
    # print("Namo negative count received: " + str(namo_negative))
    # print("Raga positive count received: " + str(raga_positive))
    # print("Raga negative count received: " + str(raga_negative))

    return "success",201


@app.route('/aboutme')
def json():
    return render_template('page1.html')


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5001)

