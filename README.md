# MultipleLinearRegressionUsingFlask
This is a simple project to elaborate how to deploy a Machine Learning model using Flask API

Project Structure
This project has four major parts :

Multiple_Linear_Regression_Wine_Quality.ipynb - 
This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'winequality-red.csv' file.

app.py -
This contains Flask APIs that receives employee details through GUI or API calls, computes the predicted value based on our model and returns it.

regresssion_model.pkl -
This is a pickle file which contains the trained model of multiple linear regression on wine quality data.

templates - 
This folder contains the HTML template (index.html) to allow user to enter employee detail and displays the predicted employee salary.

static - 
This folder contains the css folder with style.css and js files (with .js extensions) which has the styling required for out index.html file.

### Running the project

Run app.py using below command to start Flask API
    python app.py
By default, flask will run on port 5000.

### For Output : 
Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000
You should be able to view the homepage.

Enter valid numerical values in all the input boxes and hit Predict Quality.

If everything goes well, you should be able to see the predicted quality value on the same HTML page! 
Scroll down a little bit to see the output.
It is displayed below the Predict Quality button.
To confirm , make sure you see this URL in the address bar: http://127.0.0.1:5000/predict
