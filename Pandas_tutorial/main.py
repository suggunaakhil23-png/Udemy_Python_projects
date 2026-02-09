import pandas as pd

data = pd.read_csv(r"E:\Udemy Full course\Pandas_tutorial\data.csv")
fur_counts = data["Primary Fur Color"].value_counts()

data_dict = {
    "fur": fur_counts.index.tolist(),
    "count": fur_counts.values.tolist()
}

data1 = pd.DataFrame(data_dict)
data1.to_csv(r"E:\Udemy Full course\Pandas_tutorial\new_data.csv")
