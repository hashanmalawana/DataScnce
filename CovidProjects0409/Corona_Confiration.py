import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("This is how Corona_suspects-Confirmation counts ")

# Path of the file to read
Corona_suspects = open('C:/Users/hashan/CovidProjects0409/Time.csv')
# Read the file into a variable Suspect Data
Confirmation_data = pd.read_csv(Corona_suspects, index_col="date", parse_dates=True)

print(Confirmation_data)


# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Line chart showing how SearchTrend evolved over time
sns.lineplot(data=Confirmation_data)
plt.title("Corona cases confirmation reveals by date")
plt.xlabel('Date ( Withing period of announce)')
plt.ylabel('Suspects_Confirmation')
plt.show()
plt.savefig('CoronaCases.png')
