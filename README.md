# MultipleLinearRegressionUsingFlask
(https://img.shields.io/pypi/pyversions/Flask)
This is a simple project to elaborate how to deploy a Machine Learning model using Flask API

Project Structure
This project has four major parts :

1.Multiple_Linear_Regression_Wine_Quality.ipynb - <br/>
This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'winequality-red.csv' file.

2.app.py -<br/>
This contains Flask APIs that receives employee details through GUI or API calls, computes the predicted value based on our model and returns it.

3.regresssion_model.pkl -<br/>
This is a pickle file which contains the trained model of multiple linear regression on wine quality data.

4.templates - <br/>
This folder contains the HTML template (index.html) to allow user to enter employee detail and displays the predicted employee salary.

5.static - <br/>
This folder contains the css folder with style.css and js files (with .js extensions) which has the styling required for out index.html file.

### Running the project

Run app.py using below command to start Flask API<br/><br/>
      `python app.py`
By default, flask will run on port 5000.<br/>

### For Output : 
Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000<br/>
You should be able to view the homepage.<br/>

Enter valid numerical values in all the input boxes and hit **Predict Quality**.<br/><br/>

If everything goes well, you should be able to see the predicted quality value on the same HTML page! <br/>
Scroll down a little bit to see the output.<br/>
It is displayed below the Predict Quality button.<br/>
To confirm , make sure you see this URL in the address bar: http://127.0.0.1:5000/predict
