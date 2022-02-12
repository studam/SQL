# Dependencies

# Pandas
import pandas as pd

# SQL Alchemy
from sqlalchemy import create_engine
from config import Password
engine = create_engine('postgresql://postgres:Jacob@5432/Employees')
connection = engine.connect()

# MatPlotLib/NumPy/SciPy
%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as stats

employees_data = pd.read_sql("SELECT * FROM Employees", connection)
salary_data = pd.read_sql("SELECT * FROM Salaries", connection)
title_data = pd.read_sql("SELECT * FROM Titles", connection)

salary_data


plt.hist(salary_data['salary'], 20, density=False, label="Salary")
plt.axvline(salary_data['salary'].mean(), color='k', linestyle='dashed', linewidth=1, label="Salary Mean")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend() 
plt.title("Common Salary Ranges")
plt.savefig("Common Salary Ranges.png")

# query
query_into_pandas = pd.read_sql("SELECT * FROM Salaries INNER JOIN Titles ON Salaries.emp_no = Titles.emp_no", connection)

# query
avg_salaries_by_title = query_into_pandas.groupby(["title"]).mean()["salary"]

# plot, barchart
title_list = avg_salaries_by_title.index
avg_salary_for_title = avg_salaries_by_title.values

x_axis = np.arange(len(title_list))
tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, title_list, rotation=90)
plt.title("Average Salary By Title")
plt.xlabel("Title")
plt.ylabel("Average Salary ($)")
plt.grid(axis="y")
chart = plt.bar(x_axis, avg_salary_for_title, color="b", alpha=0.5, align="center")

for i in chart:
    yvalue = i.get_height()
    plt.text(i.get_x(), yvalue + 500, "${:,.2f}K".format(yvalue/1000))
    
plt.show()