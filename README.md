# Smoker Status Prediction using Bio-Signals

![Smoker Status Prediction using Bio-Signals](/smoking.jpg)

Smoking is well-documented to have a profoundly detrimental impact on human health, affecting a wide array of bodily organs and leading to the development of numerous diseases. It significantly reduces the overall life expectancy of those who smoke. As of 2018, smoking has been recognized as the leading cause of preventable morbidity and mortality worldwide, posing a persistent threat to global public health.

According to a report from the World Health Organization, it is projected that the number of deaths attributable to smoking will reach a staggering 10 million by the year 2030.

Efforts to help individuals quit smoking have been guided by evidence-based treatments, yet only a fraction of participants achieve successful abstinence. Many healthcare professionals have found counseling for smoking cessation to be ineffective and time-consuming, leading to its infrequent use in daily practice. To address this challenge, several factors have been proposed to identify smokers with a higher likelihood of quitting. These factors include the level of nicotine dependence, exhaled carbon monoxide (CO) concentration, daily cigarette consumption, age at which smoking began, past quit attempts, marital status, emotional well-being, temperament and impulsivity scores, and motivation to quit smoking. However, individual utilization of these factors for prediction can yield inconsistent and complex results, making it challenging for both healthcare providers and patients to interpret and apply the information. To simplify the process, the development of a predictive model could offer a valuable tool for estimating an individual smoker's chances of successfully quitting. Recent years have witnessed the emergence of health outcome prediction models developed using machine learning methods.

A team of scientists is currently engaged in creating predictive models with the smoking status as the target outcome. In this Project my task is to assist them in developing a machine learning model that can determine an individual's smoking status using various bio-signals.

Dataset Description:

* Age (in 5-year intervals)
* Height (in centimeters)
* Weight (in kilograms)
* Waist circumference (in centimeters)
* Eyesight in the left eye
* Eyesight in the right eye
* Hearing ability in the left ear
* Hearing ability in the right ear
* Systolic blood pressure
* Diastolic blood pressure (relaxation)
* Fasting blood sugar levels
* Total cholesterol
* Triglyceride levels
* HDL cholesterol levels
* LDL cholesterol levels
* Hemoglobin levels
* Presence of urine protein
* Serum creatinine levels
* AST (glutamic oxaloacetic transaminase) levels
* ALT (glutamic oxaloacetic transaminase) levels
* GTP (γ-GTP) levels
* Dental caries status
* Smoking status

# How to Run

## Running the app locally using virtual env

Open your command line interface.
First activate the environment inside the clone folder in your machine. Before that make sure your pipenv is already installed on your machine. If not run the following:

`pip install pipenv`

To create the virtual env with all the dependencies required for the project, run the following:

`pipenv install`

If you are having error with python version, remove the following lines from Pipfile and run the above command again:

```
[requires]
python_version = "3.10"
```

Now run the following to lock project dependencies:

`pipenv lock`

To activate the virtual environment simply run the following:

`shell pipenv`

Now start the server:

`python predict.py`

### Testing the Web Service locally using virtual environment

Once the server is on test the app using predict-test.py file:

In this file we have a test data which consists of different bio-signals collected from the patience. The data is as follows:

{'id': 2,
 'age': 40,
 'height(cm)': 165,
 'weight(kg)': 90,
 'waist(cm)': 97.8,
 'eyesight(left)': 1.2,
 'eyesight(right)': 1.5,
 'hearing(left)': '1',
 'hearing(right)': '1',
 'systolic': 132,
 'relaxation': 82,
 'fasting blood sugar': 79,
 'Cholesterol': 228,
 'triglyceride': 192,
 'HDL': 56,
 'LDL': 134,
 'hemoglobin': 16.1,
 'Urine protein': 1,
 'serum creatinine': 0.9,
 'AST': 31,
 'ALT': 40,
 'Gtp': 65,
 'dental caries': '0'}

 Based on this test data, we have to make prediction whether the patient is smoker or not.

 To make prediction, run the following:

`python predict-test.py`

## Running the app using Docker container

Add the following lines back to the Pipfile:

```
[requires]
python_version = "3.10"
```

Create the docker inside your machine.

`docker build -t smoker-prediction .`

After that, run the following to start the web service.

`docker run –it -p 9696:9696 smoker-prediction:latest`

### Testing the Web Service locally using docker

Make sure the web service is on, then simply run the following command to make prediction.

`python predict-test.py`

# Running the app from the Cloud

The app is hosted on Heroku. 

To test run the app edit the `url` variable of <a href="https://github.com/pranabsarma18/mlzoomcamp_midterm/blob/main/predict-test.py">predict-test.py</a> as follows:

`url = https://ml-zoom-docker-ab273c292374.herokuapp.com/predict`

Now, run the following command from anywhere:

`python predict-test.py`
