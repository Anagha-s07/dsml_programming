import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("tennis.csv")

# Encode categorical columns
le_outlook = LabelEncoder()
le_temp = LabelEncoder()
le_humidity = LabelEncoder()
le_wind = LabelEncoder()
le_play = LabelEncoder()

df['outlook'] = le_outlook.fit_transform(df['outlook'])
df['temp'] = le_temp.fit_transform(df['temp'])
df['humidity'] = le_humidity.fit_transform(df['humidity'])
df['wind'] = le_wind.fit_transform(df['wind'])
df['play_tennis'] = le_play.fit_transform(df['play_tennis'])

# Features and target
x = df[['outlook', 'temp', 'humidity', 'wind']]
y = df['play_tennis']

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=1
)

# Create and train model
gnb = GaussianNB()
gnb.fit(x_train, y_train)

# Test model
y_pred = gnb.predict(x_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# User input
print("\nEnter sample data")

a = input("Enter outlook: ")
b = input("Enter temp: ")
c = input("Enter humidity: ")
d = input("Enter wind: ")

# Convert input strings to encoded values
a = le_outlook.transform([a])[0]
b = le_temp.transform([b])[0]
c = le_humidity.transform([c])[0]
d = le_wind.transform([d])[0]

sample = [[a, b, c, d]]

pred = gnb.predict(sample)

# Convert prediction back to original label
print("Predicted classification:", le_play.inverse_transform(pred)[0])

