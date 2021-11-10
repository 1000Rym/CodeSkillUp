# Decorator
In this section we are going to learn decorator function.

## Decorator without tags
- P1: `@` function will automatically called when python file imported.
- P2: `func1(arg1,arg2)` = `decorated` in `deco_without_tags`.
- P3-P4: `decorated` called when `func1` calling.

```python
def deco_without_tags(func):
    """Decorator Function with out tag"""
    def decorated(*args): #P4
        print("Decorated function.")
        return func(*args) #P5 
    
    return decorated #P2 


@deco_without_tags #P1
def func1(arg1, arg2):
    print(f'{arg1}, {arg2}')

# from the function caller process(main).
func1("hello", "function1") # P3
```


## Decorator with tags
- P1: `@` will be automatically called when file is imported. 
- P2-P4: finally `func2(arg1,arg2)` = `deco_with_tags`.
- P5: Call `decorated` by referencing tag arguments.
- P6-P7: Call `decorated` function and return result.

```python
def deco_with_tags(tag1, tag2): 
    """Decorated function with tags on it."""
    def deco(func): #P3
        def decorated(*args): #P6
            print(f"decorated function with tags: {tag1}, {tag2}")
            return func(*args) #P7 
        return decorated #P4
    return deco #P2

@deco_with_tags("t1", "t2") #P1
def func2(arg1, arg2):
    print("This is function2")

# from the function caller process(main).
func1("hello", "function2") # P5
```

## Decorator with stack
- Decorator can also be called by stack structure.
- In ths case : `deco_func1`, `deco_func2`, `func_3` will be called by sequencly.

```python
@deco_func1
@deco_func2
def func_3(arg1, arg2):

# from the function caller process(main).
func3("hello", "func3")
```


