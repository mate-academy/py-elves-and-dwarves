# Сheck Your Code Against the Following Points

## Code Efficiency

1. Prevent creating a redundant list via passing comprehension without square brackets when needed.

Good example:

```python
def get_sum(numbers: list) -> int | float:
    return sum(number for number in numbers)
```

Bad example:

```python
def get_sum(numbers: list) -> int | float:
    return sum([number for number in numbers])
```

2. Do not repeat abstract methods from parent if you have an abstract class that inherits another abstract class.

Good example:

```python
class Base(ABC):
    @abstractmethod
    def say_hi(self):
        pass


class Derived(Base, ABC):
    pass


class SayHi(Derived):
    def say_hi(self):
        print("Hi!")
```

Bad example:

```python
class Base(ABC):
    @abstractmethod
    def say_hi(self):
        pass


class Derived(Base, ABC):
    @abstractmethod
    def say_hi(self):
        pass


class SayHi(Derived):
    def say_hi(self):
        print("Hi!")
```

## Code Style

1. Use one style of quotes in your code. Double quotes are preferable.
2. Use annotation, it is a good practice:

Good example:

```python
def multiply_by_2(number: int) -> int:
    return number * 2
```

Bad example:

```python
def multiply_by_2(number):
    return number * 2
```

3. Use descriptive and correct variable names:

Good example:

```python
players = ["Bob", "John"]

for player in players:
    pass
```

Bad example:

```python
players = ["Bob", "John"]

for i in players:
    pass
```

## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
