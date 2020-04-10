import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

# Path of the file to read
covid_filepath = "PatientInfo1.csv"

# Read the file into a variable covid_data
Covid_data = pd.read_csv(covid_filepath, index_col="patient_id", parse_dates=True)

print(Covid_data.columns)
print(Covid_data['age'])

spec_chars = ["s" , "@"]
for char in spec_chars:
    Covid_data['age'] = Covid_data['age'].str.replace(char, ' ')

print(Covid_data['age'])

print(type(Covid_data['age']))

