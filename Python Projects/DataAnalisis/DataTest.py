from pydoc import describe
from this import d
import pandas as pd
import numpy as np

file= 'C:\\Users\\sergi\\OneDrive\Documentos\\GitHub\\Briefcase\DataAnalisis\\COP=X.csv'
df=pd.read_csv(file)



print(df)

print(df.describe())