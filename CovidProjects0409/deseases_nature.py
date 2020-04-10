import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("This is how SearchTrend behave ")

# Path of the file to read
SearchTrend = "SearchTrend.csv"

# Read the file into a variable Search_data
Search_data = pd.read_csv(SearchTrend, index_col="date", parse_dates=True)
# Print the first 5 rows of the data
print(Search_data.head())


# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Line chart showing how SearchTrend evolved over time
sns.lineplot(hue="region", style="event" , data=Search_data)
plt.title("Search Trend of Influences as of years")
plt.xlabel('Years(2016 - 2020)')
plt.ylabel('Search Trend')
#plt.show()
plt.savefig('Searchtrends.png')
