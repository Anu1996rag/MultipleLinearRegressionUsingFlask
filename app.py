from flask import Flask,request,render_template,url_for,redirect
import numpy as np 
import pickle

# Initializing the Flask API
app = Flask(__name__)

#loading the model
model = pickle.load(open('regression_model.pkl','rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	'''
    For rendering results on HTML GUI '''
	if request.method == 'POST':
		feature_1 = request.form.get('fixed_acidity',False)
		feature_2 = request.form.get('volatile_acidity',False)
		feature_3 = request.form.get('citric_acid',False)
		feature_4 = request.form.get('residual_sugar',False)
		feature_5 = request.form.get('chlorides',False)
		feature_6 = request.form.get('free_sulfur_dioxide',False)
		feature_7 = request.form.get('total_sulfur_dioxide',False)
		feature_8 = request.form.get('density',False)
		feature_9 = request.form.get('pH',False)
		feature_10 = request.form.get('sulphates',False)
		feature_11 = request.form.get('alcohol',False)
		#converting all the features into float if they were to receive the integer values 
		final_features = np.array([feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,feature_7,feature_8,feature_9,feature_10,feature_11],np.float64).reshape(1,-1) #converting the form values into numpy array
		prediction = model.predict(final_features)
		predicted = prediction[0] #taking out the initial value
		output = round(float(predicted),2) #converting the np.ndarray value to float and then rounding upto 2 floating places after decimal point
		
		return render_template('index.html',fixed_acidity=feature_1,volatile_acidity=feature_2,citric_acid=feature_3,residual_sugar = feature_4,chlorides=feature_5,free_sulfur_dioxide=feature_6,total_sulfur_dioxide=feature_7,density=feature_8,pH=feature_9,sulphates=feature_10,alcohol=feature_11, prediction_text ="Quality of wine : {}".format(output))
	else:
		return render_template('index.html')

	

if __name__ == "__main__":
    app.run(debug=True)