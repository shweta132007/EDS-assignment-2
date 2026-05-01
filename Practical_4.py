#PRACTICAL 4

#Question 4.1.1. 
#Pandas - series creation and manipulation
#code:
import pandas as pd

# Take inputs from the user to create a list of numbers
numbers = list(map(int, input().split()))

# Create a Pandas series from the list of numbers
series=pd.Series(numbers)
# Grouping by even and odd numbers and calculating the mean
grouped = series.groupby(series % 2==0).mean()

# Display the mean of even and odd numbers with labels
grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]
print("Mean of even and odd numbers:")
print(grouped)



#4.1.2. 
#Dictionary to dataframe
#code:
import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
new_name=input("New name: ")
new_age=int(input("New age: "))
df.loc[len(df)] = [new_name, new_age]
# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row
modify_index = int(input("Index of row to modify: "))
new_age_value = int(input("New age: "))
df.loc[modify_index,'Age'] = new_age_value

# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row
delete_index = int(input("Index of row to delete: "))
df = df.drop(delete_index).reset_index(drop=True)

# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column
genders = input("Enter genders separated by space: ").split()
df['Gender']=genders


# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
df['Name'] = df['Name'].str.upper()

# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df = df.drop('Age',axis=1)
# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)



# Question 4.1.3.
#Student Information
#code:
import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# write your code here..

print("First five rows:")
print(data.head())

avg_age = round(data["Age"].mean(), 2)
print("Average age:", avg_age)

filtered_data = data[data["Grade"]<="B"]

print("Students with a grade up to B")
print(filtered_data)




# Question 4.2.1
#Month with the Highest Total Sales
#code:
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
df['Sales'] = df['Quantity'] * df['Price']
monthly_sales = df.groupby('Month')['Sales'].sum()

# Find best month
best_month =monthly_sales.idxmax()
highest_sales = monthly_sales.max()

print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")





# Question 4.2.2
#bset selling product
#code:
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
product_sales=df.groupby("Product")["Quantity"].sum()

# Find the product with the highest total quantity sold
best_product =product_sales.idxmax()
highest_quantity = product_sales.max()

# Display the result
print(f"Best selling product: {best_product}")
print(f"Total quantity sold: {highest_quantity}")



#Question 4.2.3
#city that sold most product
#code:
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
product_sold=df.groupby("City")["Quantity"].sum()
best_city=product_sold.idxmax()

# Display the result
print(f"City sold the most products: {best_city}")



# Question 4.2.4
#most frequently sold product pairs
#code:
import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code


# Output the most frequent product pairs
grouped = df.groupby('Date')['Product'].apply(list)

pair_counter = Counter()

for products in grouped:
    unique_products = list(set(products))
    pairs = combinations(sorted(unique_products), 2)
    pair_counter.update(pairs)

max_count = max(pair_counter.values())

for pair, count in pair_counter.items():
    if count == max_count:
        print(f"{pair[0]} and {pair[1]}: {count} times")




# Question 4.2.5
# Titanic Dataset Analysis and Data Cleaning
#code:
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# 1. Display the first 5 rows of the dataset
print(data.head())

# 2. Display the last 5 rows of the dataset

print(data.tail())

# 3. Get the shape of the dataset (number of rows and columns)

print(data.shape)

# 4. Get a summary of the dataset using .info()
data.info()

# 5. Get basic statistics (mean, standard deviation, etc.) of the dataset using .describe()
print("None")
print(data.describe())

# 6. Check for missing values and display the count of missing values for each column
print(data.isnull().sum())

# 7. Fill missing values in the 'Age' column with the median age
median_age =data['Age'].median()
data['Age'].fillna(median_age, inplace=True)

# 8. Fill missing values in the 'Embarked' column with the most frequent value (mode)
mode_embarked = data['Embarked'].mode()[0]
data['Embarked'].fillna(mode_embarked, inplace=True)

# 9. Drop the 'Cabin' column due to many missing values
data.drop(columns=['Cabin'], inplace=True)

# 10. Create a new column 'FamilySize' by adding the 'SibSp' and 'Parch' columns
data['FamilySize'] = data['SibSp'] + data['Parch']




# question  
#Titanic Dataset Analysis and Data Cleaning - 2
#code:
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']

# 1. Create a new column ‘IsAlone' (1 if alone, 0 otherwise)
data['IsAlone'] = np.where(data['FamilySize'] == 0, 1, 0)

# 2. Convert ‘Sex' to numeric (male: 0, female: 1)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 3. One-hot encode the ‘Embarked' column (drop first category)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 4. Get the mean age of passengers
mean_age = data['Age'].mean()
print(mean_age)

# 5. Get the median fare of passengers
median_fare = data['Fare'].median()
print(median_fare)

# 6. Get the number of passengers by class
pclass_count = data['Pclass'].value_counts()
print(pclass_count)

# 7. Get the number of passengers by gender
gender_count = data['Sex'].value_counts()
print(gender_count)

# 8. Get the number of passengers by survival status
survival_count = data['Survived'].value_counts()
print(survival_count)

# 9. Calculate the survival rate
survival_rate = data['Survived'].mean()
print(survival_rate)

# 10. Calculate the survival rate by gender
survival_by_gender = data.groupby('Sex')['Survived'].mean()
print(survival_by_gender)



#question 4.2.7. 
#Titanic Dataset Analysis and Data Cleaning - 3
#code:
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Calculate the survival rate by class
survival_by_class = data.groupby('Pclass')['Survived'].mean()
print(survival_by_class)

# 2. Calculate the survival rate by embarked location (Embarked_S)
survival_by_embarked = data.groupby('Embarked_S')['Survived'].mean()
print(survival_by_embarked)

# 3. Calculate the survival rate by family size
survival_by_family = data.groupby('FamilySize')['Survived'].mean()
print(survival_by_family)

# 4. Calculate the survival rate by being alone
survival_by_alone = data.groupby('IsAlone')['Survived'].mean()
print(survival_by_alone)

# 5. Get the average fare by passenger class
avg_fare_by_class = data.groupby('Pclass')['Fare'].mean()
print(avg_fare_by_class)

# 6. Get the average age by passenger class
avg_age_by_class = data.groupby('Pclass')['Age'].mean()
print(avg_age_by_class)

# 7. Get the average age by survival status
avg_age_by_survival = data.groupby('Survived')['Age'].mean()
print(avg_age_by_survival)

# 8. Get the average fare by survival status
avg_fare_by_survival = data.groupby('Survived')['Fare'].mean()
print(avg_fare_by_survival)

# 9. Get the number of survivors by class
survivors_by_class = data[data['Survived'] == 1]['Pclass'].value_counts()
print(survivors_by_class)

# 10. Get the number of non-survivors by class
nonsurvivors_by_class = data[data['Survived'] == 0]['Pclass'].value_counts()
print(nonsurvivors_by_class)


# Question 4.2.8.
#Titanic Dataset Analysis and Data Cleaning - 4
#code:
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Get the number of survivors by gender
survivors_by_gender = data[data['Survived'] == 1]['Sex'].value_counts()
print(survivors_by_gender)

# 2. Get the number of non-survivors by gender
nonsurvivors_by_gender = data[data['Survived'] == 0]['Sex'].value_counts()
print(nonsurvivors_by_gender)

# 3. Get the number of survivors by embarked location (Embarked_S)
survivors_by_embarked = data[data['Survived'] == 1]['Embarked_S'].value_counts()
print(survivors_by_embarked)

# 4. Get the number of non-survivors by embarked location (Embarked_S)
nonsurvivors_by_embarked = data[data['Survived'] == 0]['Embarked_S'].value_counts()
print(nonsurvivors_by_embarked)

# 5. Calculate the percentage of children (Age < 18) who survived
children = data[data['Age'] < 18]
children_survival_rate = children['Survived'].mean()
print(children_survival_rate)

# 6. Calculate the percentage of adults (Age >= 18) who survived
adults = data[data['Age'] >= 18]
adults_survival_rate = adults['Survived'].mean()
print(adults_survival_rate)

# 7. Get the median age of survivors
median_age_survivors = data[data['Survived'] == 1]['Age'].median()
print(median_age_survivors)

# 8. Get the median age of non-survivors
median_age_nonsurvivors = data[data['Survived'] == 0]['Age'].median()
print(median_age_nonsurvivors)

# 9. Get the median fare of survivors
median_fare_survivors = data[data['Survived'] == 1]['Fare'].median()
print(median_fare_survivors)

# 10. Get the median fare of non-survivors
median_fare_nonsurvivors = data[data['Survived'] == 0]['Fare'].median()
print(median_fare_nonsurvivors)

