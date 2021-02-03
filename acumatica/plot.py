import pandas as pd
data = input("File?:")
df = pd.read_csv(data)
import matplotlib.pyplot as plt
df.plot(x="Name", y="Cost", kind="barh")
plt.show()
exit()
