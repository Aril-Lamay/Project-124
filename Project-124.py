from flask import Flask,jsonify,request

app = Flask(__name__)
data = [{
    "Contact" : "9470961735",
    "Name" : "Raj",
    "done" : False,
    "id" : 1
},
{
    "Contact" : "9430379079",
    "Name" : "Kabir",
    "done" : False,
    "id" : 2
}]

@app.route('/add-data',methods = ["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "Status" : "error",
            "message" : "Please provide data"
        },400)
    
    dt = {
        "Contact" : request.json["Contact"],
        "Name" : request.json["Name"],
        "done" : False,
        "id" : data[-1]["id"]+1
    }
    data.append(dt)
    return jsonify({
        "status " : "Success",
        "message " : "Task added successfully"
    })

@app.route('/get-data')
def get_data():
    return jsonify({
        "data" : data
    })

if(__name__ == '__main__'):
    app.run(debug = True)