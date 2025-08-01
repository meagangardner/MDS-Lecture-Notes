## Copy the Code to the Workspace

What column gives you a mean of 63.4?

* Column 1

What is the mean of Column 3?

* 47.4

Organise the columns from highest mean to lowest mean (highest at the top).

* Column 1
* Column 3
* Column 2

## Multiple Choice Example

Why are categoricals in Python, particularly in libraries like pandas, useful for data science and analysis? (Select all that apply)

Correct answers:

* They reduce memory usage and improve performance by storing repeated values more efficiently.

* They improve the performance of certain operations, such as groupby and sorting, by leveraging the categorical nature of the data.

* They allow categories to be ordered, which is useful for mapping attributes like color or size to category levels in plots.


## Coding Example 1

Solution:

```python
train_data = pd.read_csv('training_data.csv', sep=';')
```

## Coding Example 2

Solution:

```python
manu_large_old_planes = planes.query("year < 1999 & seats == 182")[['manufacturer']]
```
