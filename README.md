# My Awesome EDA Module
Welcome to the My Awesome EDA (Exploratory Data Analysis) Module! This Python module provides a set of tools for exploring and analyzing your dataset. Whether you're a data scientist, analyst, or enthusiast, this module will help you gain insights into your data quickly and efficiently.

## Features
- **Welcome Gif**: A fun welcome gif to kick off your exploration.
- **Basic Dataset Information**: Quickly get an overview of the number of observations (rows) and parameters (columns) in your dataset.
- **Data Type Summary**: Understand the data types of each column in your dataset.
- **Categorization of Features**: Categorize features into numerical, string, and categorical based on unique threshold.
- **Summary Statistics**: Get descriptive statistics for numerical features, including mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum values.
- **Outliers Detection**: Identify outliers in numerical features using the interquartile range (IQR) method.
- **Missing Values Analysis**: Investigate missing values in your dataset, including total missing values, rows with missing values, and columns with missing values.
- **Duplicate Rows Detection**: Identify duplicate rows in your dataset.
- **Visualizations**: Generate informative visualizations including bar plots of missing values by variable, correlation heatmap for numerical features, and histograms with boxplots for numerical features.

## Installation
```bash
git clone https://github.com/iliapopov17/MyAwesomeEDA.git
```

```bash
pip install -r requirements.txt
```

## Usage Guide

### GIF format

<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/demo/imgs/demo.gif" align='center', width="100%">
</div>

### Markdown fomat

```python
import pandas as pd
from my_awesome_eda import run_eda
```

```python
df = pd.read_csv('data/titanic.csv')
```

```python
run_eda(df)
```

```python
Unique threshold for categorical features: # you need to manually input a number - threshold to categorize features to categorical features
```

```
Welcome to the Awesome EDA Module!
```

<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/img/welcome.gif" align='center', width="50%">
</div>

```
Number of observations (rows):
891
Number of parameters (columns):
12

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Data types of each column:
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
SibSp            int64
Parch            int64
Ticket          object
Fare           float64
Cabin           object
Embarked        object

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Numerical features:
['PassengerId', 'Age', 'SibSp', 'Parch', 'Fare']

String features:
['Name', 'Ticket', 'Cabin']

Categorical features:
['Survived', 'Pclass', 'Sex', 'Embarked']

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Counts and frequencies for Survived:
0: Counts=549, Frequencies=61.62%
1: Counts=342, Frequencies=38.38%

Counts and frequencies for Pclass:
3: Counts=491, Frequencies=55.11%
1: Counts=216, Frequencies=24.24%
2: Counts=184, Frequencies=20.65%

Counts and frequencies for Sex:
male: Counts=577, Frequencies=64.76%
female: Counts=314, Frequencies=35.24%

Counts and frequencies for Embarked:
S: Counts=644, Frequencies=72.28%
C: Counts=168, Frequencies=18.86%
Q: Counts=77, Frequencies=8.64%

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Summary statistics for numerical features:
       PassengerId         Age       SibSp       Parch        Fare
count   891.000000  714.000000  891.000000  891.000000  891.000000
mean    446.000000   29.699118    0.523008    0.381594   32.204208
std     257.353842   14.526497    1.102743    0.806057   49.693429
min       1.000000    0.420000    0.000000    0.000000    0.000000
25%     223.500000   20.125000    0.000000    0.000000    7.910400
50%     446.000000   28.000000    0.000000    0.000000   14.454200
75%     668.500000   38.000000    1.000000    0.000000   31.000000
max     891.000000   80.000000    8.000000    6.000000  512.329200

Outliers count for numerical features:
Outliers count for PassengerId: 0
Outliers count for Age: 11
Outliers count for SibSp: 46
Outliers count for Parch: 213
Outliers count for Fare: 116

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Total missing values:
866
Rows with missing values:
708
Columns with missing values:
['Age', 'Cabin', 'Embarked']

Number of duplicate rows:
0

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====
```
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/demo/imgs/1.png" align='center', width="50%">
</div>

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/demo/imgs/2.png" align='center', width="50%">
</div>

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/demo/imgs/3.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/demo/imgs/4.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/demo/imgs/5.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/demo/imgs/6.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/MyAwesomeEDA/blob/main/demo/imgs/7.png" align='center', width="50%">
</div>

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Also there is `demo.ipynb` file in this repository. Download and try it yourself!
