# Smoker Status Prediction using Bio-Signals

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

First activate the env inside the clone folder in your machine.

Make sure your machine already installed pipenv.

`shell pipenv`

Then, create the docker inside your machine.

`docker build -t <tag_name> .`

After that, run the following to start the churn web service.

`docker run –it –-rm -p 9696:9696 <tag_name>`

Note: If the docker daemon is not running, run the following code.

`sudo dockerd`

# Testing the Web Service locally

Make sure the web service is on, then simply run the following code.

`python predict-test.py`

# Running the app from the Cloud

The app is hosted on Heroku. To test run the app edit the `url` variable of predict-test.py as:

`url = https://ml-zoom-docker-ab273c292374.herokuapp.com/predict`
