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
git clone https://github.com/iliapopov17/EDA-module.git
```

## Usage

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
<img src="https://github.com/iliapopov17/EDA-module/blob/main/img/welcome.gif" align='center', width="50%">
</div>

```
Number of observations (rows):
887
Number of parameters (columns):
8

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Data types of each column:
Survived                     int64
Pclass                       int64
Name                        object
Sex                         object
Age                        float64
Siblings/Spouses Aboard      int64
Parents/Children Aboard      int64
Fare                       float64

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Numerical features:
['Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare']

String features:
['Name']

Categorical features:
['Survived', 'Pclass', 'Sex']

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Counts and frequencies for Survived:
0: Counts=545, Frequencies=61.44%
1: Counts=342, Frequencies=38.56%

Counts and frequencies for Pclass:
3: Counts=487, Frequencies=54.90%
1: Counts=216, Frequencies=24.35%
2: Counts=184, Frequencies=20.74%

Counts and frequencies for Sex:
male: Counts=573, Frequencies=64.60%
female: Counts=314, Frequencies=35.40%

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Summary statistics for numerical features:
              Age  Siblings/Spouses Aboard  Parents/Children Aboard       Fare
count  887.000000               887.000000               887.000000  887.00000
mean    29.471443                 0.525366                 0.383315   32.30542
std     14.121908                 1.104669                 0.807466   49.78204
min      0.420000                 0.000000                 0.000000    0.00000
25%     20.250000                 0.000000                 0.000000    7.92500
50%     28.000000                 0.000000                 0.000000   14.45420
75%     38.000000                 1.000000                 0.000000   31.13750
max     80.000000                 8.000000                 6.000000  512.32920

Outliers count for numerical features:
Outliers count for Age: 13
Outliers count for Siblings/Spouses Aboard: 46
Outliers count for Parents/Children Aboard: 213
Outliers count for Fare: 116

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====

Total missing values:
0
Rows with missing values:
0
Columns with missing values:
[]

Number of duplicate rows:
0

===== ===== ===== ===== ===== =====
===== ===== ===== ===== ===== =====
```
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/EDA-module/blob/main/img/demo/1.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/EDA-module/blob/main/img/demo/2.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/EDA-module/blob/main/img/demo/3.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/EDA-module/blob/main/img/demo/4.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/EDA-module/blob/main/img/demo/5.png" align='center', width="50%">
</div>
<div style='justify-content: center'>
<img src="https://github.com/iliapopov17/EDA-module/blob/main/img/demo/6.png" align='center', width="50%">
</div>

Also there is `demo.ipynb` file in this repository. Download and try it yourself!
