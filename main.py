# from keras.models import load_model
# import h5py
# expression = load_model('./model/expression_model.hdf5')

from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"if __name__ == "__main__":        # on running python app.py

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    params = flask.request.json
    
    if (params != None):
        return params

app.run()                    # run the flask app
  