## Basic
### Variables
- `var varName = value;`

### I/O
- Output
    - `alert("value to print")`
    - `console.log("value to print")`
- Input
    - `var value = promt("Input your value:")`

### How to connecting Javascript?
- Under the html add `<script scr='scriptname.js'></script>` to connecting Javascript.
- example_code: [example1.html](example1.html), [example1.js](example1.js).
- exercise: [exercise1.html](exercise1.js), [exercise1.js](exercise1.js).

### DataTypes
- `Number`: All kinds of numbers are treated as numbers type.
- `String`
    - Support concant by using `+`
    - index : `"mystring"[5]`  -> `i`
- `Boolean`: `true`, `false`
- `undefined` and `null`, `NaN`

### Operation
- Arithmetic Operators: `+`,`-`,`*`,`/`,`%`, `++`, `--`.
- Assignment Operators: `=`, `+=`, `-=`, `*=`, `/=`, `%=`.
- String Operators: `+`, `+=`.
- Comparison Operators: `==`, `===`, `!=`, `!==`, `>`, `<`, `>=`, `<=`.
    - `===` and `!==` will also check the type, which `==`, `!=` don't consider.
- Conditional (Ternary) Operator: `var1 = (condition)? val2:val3`.
- Logical Operators: `&&`, `||`, `!`.
- Bitswise Operators: `&`, `|`, `~`, `^`, `<<`, `>>`.
- Other Operators: `typeof`, `delete`, `in`, `instanceof`, `void`.
    - `void` operators evaluates an expression and returns `undefined`.

### Control Flow
- Conditional Statement
    - ```javascript
        if(condition1){
            ...
        }else if(condition2){
            ...
        }else{
            ...
        }
      ```
- While Loop:
    -   ```javascript
        while(condition){
            //execute the command while it is fit condition, not break
        }
        ```
- For Loop([exercise_for_loop.html](exercise_for_loop.html)):
    - For
        ```javascript
        for(statement1; statement2; statement3){
            //execute the command
        }
        ```
    - For/In : Loops through the key from the object.
        ```javascript
        for (var key in object){
            object[key]
        }
        ```

    - For/of : Loops through values of an iterable object.
        ```javascript
        for (var element_value of list_or_dicts){
            element_value
        }

### Function:
```javascript
function func_name(parameter1='default_value', paramenter2){
    //code to execute
    var local_var; //local variable
    return local_var;
}

var global_var = func_name(a, b)
```

- exercise: [exercise2_function.js](exercise2_function.js)

### Array: 
- define an array:  
    ```javascript
    // normal array
    cuontries = ["korea","usa","england"]
    // mixed array
    matrix = [[1,2,3],[11,22,33],[111,222,333]]
    ```
- method:
    - `lenght` : lenght of the array.
    - `pop()` : pop the last item of the array.
    - `push(item)`: push the item in the array.
    - `splice(start, deletecCount(option), items(option)...)`: changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.
    - `slice(start(option), end(option))`: returns a shallow copy of a portion of an array into a new array object selected from start to end (end not included) where start and end represent the index of items in that array
    - `foreach`: run the function of each array, each element will passed as the parameter.
        - Use built-in method: `countries.foreach(alert)`
        - Use customized method: 
            - define function under the parameter: `countries.foreach(function mySum(item){...})`
            - use defined function: `countries.foreach(mySum)`
        - Modify array's value: 
            ```javascript
            numbers = [1,2,3,4,5]
            numbers.foreach(myFunction)
            function myFunction(item, index, arr){
                arr[index] = item * 10;
            }
            ```
    - other methods need to know: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

- array exercise: [exercise3_array.js](exercise2_function.js)

### Object
- Object is constructed with `key` and `value`
- Use `for in` loop to access and modify the Object.
- Support nested value. 
- Define function by `key: function(){...}`

```javascript
// Note that the key dosn't need "".
CarInfo = { vendor: "Toyota", country: "Japan", date: 2017
            intro: function(){
                return "This car is made by " + this.vendor+ " in"
                this.country + " on " + this.date;
            }
          }

// However to access the value, we need to add "".  
CarInfo["vendor"] = "Kia";
```
- code: [exercise4_object.js](exercise4_object.js)


## When to add semicolons?
- Semicolons in JavaScript is optional because of __ASI__(automatic semicolon insertion).
- ASI Rules:
    - When an offending token is encountered that is not allowed by the grammar, a semicolon is inserted before it if:
        - The token is separated from the previous token by at least one __LineTerminator__.
        - The token is `}`
- ASI Notable:
    - About `return` expression
        ```javascript
        function getCheese(){
            //Incorrect
            return  //This line is known as return
            {
                    cheeseType:"Gouda"
            }

            //correct : return statement should begin on same line, like this:
            return {
                cheeseType :"Gouda"
            }
        }
        ```
    - When should I __Not Use__ Semicolons?
        - `if(...){...}else{...}`
        - `for(...){...}`
        - `while(...){...}`





#### Reference
- Semicolons in JavaScript: To Use or Not to Use?: https://dev.to/adriennemiller/semicolons-in-javascript-to-use-or-not-to-use-2nli
- Javascript Opeprator: https://www.w3schools.com/jsref/jsref_operators.asp
