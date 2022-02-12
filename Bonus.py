import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# Import DB user and password
from api_keys import pgadim_user
from api_keys import pgadim_pass

database_url = f"postgresql://{pgadim_user}:{pgadim_pass}@localhost:5432/sql-challenge"

from sqlalchemy import create_engine
engine = create_engine(database_url)
connection = engine.connect()

# Salary dataframe
salary_df = pd.read_sql("SELECT * FROM salaries", engine)
salary_df

# Look for NAN values
salary_df.isnull().values.any()

# Create a histogram to visualize the most common salary ranges for employees.
ax = salary_df.hist(column='salary', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)

ax = ax[0]
for x in ax:


    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", 
                  left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # Remove title
    x.set_title("")

    # Set x-axis label
    x.set_xlabel("Salary ($)", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel("Frequency", labelpad=20, weight='bold', size=12)
    
    # Set y-axis label
    x.set_title("Salary Distribution", weight='bold', size=14)

    # Format y-axis label
    x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
    
plt.savefig('Salary_Distribution.png')


# Salary by Title
salary_grop_df = pd.read_sql("""SELECT titles.title, AVG(salaries.salary)
                        FROM employees
                        JOIN salaries 
                        ON employees.emp_no = salaries.emp_no
                        JOIN titles
                        ON titles.emp_title_id = employees.emp_title_id
                        GROUP BY titles.title""", engine)

salary_grop_df

# Look for NAN values
salary_grop_df.isnull().values.any()

# Create a bar chart of average salary by title
ax = salary_grop_df.plot.bar(x='title', y='avg', rot=90, grid=False, figsize=(10,8), color='#86bf91', zorder=2)

# Switch off ticks
x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", 
                  left="off", right="off", labelleft="on")

# Draw horizontal axis lines
vals = x.get_yticks()
for tick in vals:
    x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

ax.get_legend().remove()

# Set x-axis label
ax.set_xlabel("Title", labelpad=20, weight='bold', size=12)

# Set y-axis label
ax.set_ylabel("Salary ($)", labelpad=20, weight='bold', size=12)
    
# Set y-axis label
ax.set_title("Average Salary by Title", weight='bold', size=14)

# Format y-axis label
ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

plt.tight_layout()

plt.savefig('Average_Salary_Title.png')

your_salary = pd.read_sql("""SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
                            FROM employees
                            JOIN salaries ON employees.emp_no = salaries.emp_no
                            WHERE employees.emp_no = 499942""", engine)

your_salary

