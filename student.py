import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
marks=np.array([50,80,85,30,79])
data={"student":['teja','bunny','sunny','ramu','raghu'],
      'Marks':marks
      }
df=pd.DataFrame(data)
plt.bar(df["student"],df["Marks"],color='green')
plt.xlabel('student')
plt.ylabel('Marks')
plt.title("student marks analysis")
plt.legend()
plt.show()