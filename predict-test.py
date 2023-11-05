import requests

url = 'http://localhost:9696/predict'

patient = {'id': 2,
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

response = requests.post(url, json=patient).json()
print(response)

if response['smoker'] == True:
    print('The patient is a Smoker')
else:
    print('The patient is not a Smoker')