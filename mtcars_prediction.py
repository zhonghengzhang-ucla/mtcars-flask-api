import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('mtcars.csv')
df = df.drop(columns='model')

predictors = df.drop(columns='mpg').columns.tolist()

model = LinearRegression()
model.fit(df.drop(columns='mpg'), df['mpg'])

def predict(input: dict) -> float:
    X = pd.DataFrame(input, index=[0], dtype=float)[predictors]
    y = model.predict(X)[0]
    return y
