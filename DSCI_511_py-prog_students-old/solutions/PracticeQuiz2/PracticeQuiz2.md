# Solutions to Practice Quiz2

## Why use linters

To detect potential errors and enforce coding standards

## Calling a parent method

```
super().can_fly()
```

## Modify a for loop

```
sum = 0
for x in range(1, 11):
  if x % 2 == 0:
    sum += x
print(sum)
```

## Add string method to Book class

```
class Book:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} by {self.author} ({self.year})'
```

## Add highest method to Food class

```
class Food:
        
    def __init__(self, folate, potassium):
        self.folate = folate
        self.potassium = potassium
    
    def highest(self):
        if self.folate > self.potassium:
        	return 'Folate'
        else:
        	return 'Potassium'
```
