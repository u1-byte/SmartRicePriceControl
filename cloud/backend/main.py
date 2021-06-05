import os
from predict import *
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/crops_predict', methods=['GET'])
def predict():
    try:
        data1 = float(request.args.get('param1'))
        data2 = float(request.args.get('param2'))
        data3 = float(request.args.get('param3'))
        data4 = float(request.args.get('param4'))
        data5 = float(request.args.get('param5'))
        data6 = float(request.args.get('param6'))
        data7 = float(request.args.get('param7'))
        data8 = float(request.args.get('param8'))
        data9 = float(request.args.get('param9'))
        data10 = float(request.args.get('param10'))
        data11 = float(request.args.get('param11'))
        data12 = float(request.args.get('param12'))
        data13 = float(request.args.get('param13'))
        data14 = float(request.args.get('param14'))
        data = [data1, data2, data3, data4, data5, data6, data7,
                 data8, data9, data10, data11, data12, data13, data14]
    except:
        data = [[]]
    results = {
        "Produksi": 0.0,
    }
    print(data)
    # checking input
    if len(data) != 14:
        return jsonify(results)
    for nilai in data:
        if str(type(nilai)) != "<class 'float'>":
            return jsonify(results)

    model_location = 'gs://rice_price_dev/ml_models/test_model_r2.h5'
    input_fit_data = [[26.49, 26.49, 26.49, 26.49, 67, 67, 67, 67, 0, 0, 0, 0, 3.27, 333],
                  [30.25, 30.25, 30.25, 30.25, 85.45, 85.45, 85.45, 85.45, 18.84, 18.84, 18.84, 21.84, 9.47, 29694]]  # need to change this
    output_fit_data = [[1194.46], [103583.39]]
    
    prediction = predict(input_fit_data,output_fit_data,data,model_location)

    results["Produksi"] = float(prediction[0])

    json_results = jsonify(results)
    return json_results

@app.route('/api/temp_predict', methods=['GET'])
def pred_temp():
    return pred_temp()

@app.route('/api/hum_predict', methods=['GET'])
def pred_hum():
    return pred_hum()

@app.route('/api/rain_predict', methods=['GET'])
def pred_rain():
    return pred_rain()

@app.route('/api/shine_predict', methods=['GET'])
def pred_shine():
    return pred_shine()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get("PORT", 8080)))