## Python Testing
Automated testing is the execution of your __test plan__ by script instead of human.
- Test Plan: The parts of yhour application you want to test, __the order__ in which you want to test them, and the __expected response__.

- Basic Concept of testing: 
    - Integeration testing : test steps + test assertions.
        - Checks components in your application operate with each other.
    - Unit Test: A smaller test, one that checks that a single compenent operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.
        - Checks a small component in your application.

- REPL example:
    ```python
    assert sum([1,2,3]) = 6, "Should be 6" 
    ```

- Normal example without test runner: [without_test_runner.py](without_test_runner.py)

### Choosing a test runner
- unitest (The one built in to python standard library)
- nose or nose2
- pytest

#### unittset
- Has been built into the python standard library since the version 2.1.
- Contains testing framwork and test runner.
- Requires the following:
    - Put your tests in to the classes as methos
    - Use Assertion methods in the unitest.TestCase class.
- Exmaple Code: [with_unittest.py](with_unittest.py)
    - Be careful when calling in Python2.7 below.(It will call different versioncalling `unittest2`)

#### nose
Nose is compatible with any tests wrriten using the unittest framework and used as drop-in replacement for the unitest test runner(Recommended use node2)
- Test files name should start with prefix `test_`.
    ```shell
    $pip3 install nose2
    nose2
     -v  # or $python -m nose2
    ```

    ```shell
    cheonlim@MacBook-Pro how_to_test % nose2
    .F.F
    ======================================================================
    FAIL: test_without_test_runner.test_sum_tuple
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/Users/cheonlim/Developing/PlayGround/CodeSkillUp/python/FluentPython/how_to_test/test_without_test_runner.py", line 8, in test_sum_tuple
        assert sum((1,2,2)) == 6, "should be 6"
    AssertionError: should be 6

    ======================================================================
    FAIL: test_sum_tuple (test_with_unittest.TestSum)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/Users/cheonlim/Developing/PlayGround/CodeSkillUp/python/FluentPython/how_to_test/test_with_unittest.py", line 11, in test_sum_tuple
        self.assertEqual(sum((1,2,2)), 6, "Shold be 6.")
    AssertionError: 5 != 6 : Shold be 6.

    ----------------------------------------------------------------------
    Ran 4 tests in 0.000s
    ```


### pytest
Same with nose pytest also supports execution of unittest testcases.Runs series functiosn in a Python starting with the name `test_`. GUI is more friendly than nose
-   Environment setup and execution
    ```shell
    $pip3 install pytest
    pytest
    ```
-   Environment setup and execution
    ```shell
    cheonlim@MacBook-Pro how_to_test % pytest
    ================================ test session starts =================================
    platform darwin -- Python 3.8.4, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
    rootdir: /Users/cheonlim/Developing/PlayGround/CodeSkillUp/python/FluentPython/how_to_test
    collected 4 items

    test_with_unittest.py .F                                                       [ 50%]
    test_without_test_runner.py .F                                                 [100%]

    ====================================== FAILURES ======================================
    _______________________________ TestSum.test_sum_tuple _______________________________

    self = <test_with_unittest.TestSum testMethod=test_sum_tuple>

        def test_sum_tuple(self):
    >       self.assertEqual(sum((1,2,2)), 6, "Shold be 6.")
    E       AssertionError: 5 != 6 : Shold be 6.

    test_with_unittest.py:11: AssertionError
    ___________________________________ test_sum_tuple ___________________________________

        def test_sum_tuple():
    >       assert sum((1,2,2)) == 6, "should be 6"
    E       AssertionError: should be 6
    E       assert 5 == 6
    E        +  where 5 = sum((1, 2, 2))

    test_without_test_runner.py:8: AssertionError
    ============================== short test summary info ===============================
    FAILED test_with_unittest.py::TestSum::test_sum_tuple - AssertionError: 5 != 6 : Sh...
    FAILED test_without_test_runner.py::test_sum_tuple - AssertionError: should be 6
    ============================ 2 failed, 2 passed in 0.19s =============================
    ```

### Simple Test Project
How to Structure a Simple Test? 

- Consideration before decisions:
    -  what to test?
    -  unit test or itegration test?
- Structure of test should loosely follw:
    1. create inputs
    2. execute the code being tested, caputring the output
    3. compare output with the expected results.

- Example is descripted by follwoing structure: 
    - project/
        -  my_sum/
            - [`__init__.py`](__init__.py)
        - [test.py](test_sum.py)

#### Executing
```shell
# Test with unit test
$ python3 -m unittest test
$ python3 -m unittest -v test # Input verbose
$ python3 -m unittest discover # Search anyfiles names test*.py
$ python3 -m unittest discover -s tests # Tag name of the directory.
$ python3 -m unittest discorver -s tests -t src # Tag sub directory. 
```

### Supported Assertions
- `.assertEqaul(a,b)` : a==b
- `.assertTrue(x)`, `.assertFalse(x)` : bool(x) is True, False
- `.assertIs(a, b)`,`.assertIsNot(a, b)`: a is b, a is not b
- `.assertIsNone(x)`, `.assertIsNotNone(x)`: x is None, x is not None
- `.assertIn(a,b), .assertNotIn(a, b)`: a in b, a is not in b
- `.assertInstance(a, b)`, `.assertNotIsInstance(a,b)`: isinstance(a,b), not isinstance(a,b)

### Integrating Tests
Integration testing is the testing of multiple components of application to check that they work together.
Example of Construct Data-Driven Applications: 
- Project/
    - my_app/
        - `__init__.py`
    - tests/
        - unit/
            - `__init__.py`
            - test_unit.py
        - integration/
            - `__init__.py`
            - test_integration.py

In the Integration test use `setup()` method to setup the TestCase.

- Example Code:
```python
class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load testdata
        self.app = App(database = 'fixtures/test_basic.json')

```

### Futher Things to Know

#### Test in Multiple Environment
Use __tox__ to test in multiple environment.
- How to Setup
    ```shell
    $pip install tox
    $tox-quickstart
    ```
- Will be updated later. 

#### Test Automatically
Travis CI is one of CI available CI(Continuous Integration) tools.
```YAML
# script under the .travis.yml
language: python
python :
    - "2.7"
    - "3.7"
install : 
    - pip install -r requirements.txt
    - python -m unittest.discover
```

#### Testing for Performance Degradation Between Changes
Tools: pytest-benchmark
```python
def test_my_function():
    result =benchmark(test)
```

#### Testing for Security in your Application
Tools: bandit
```shell
$ pip install bandit
$ bandit -r my_sum
```


### Reference
- Python Testing : https://realpython.com/python-testing/
- unittest: https://docs.python.org/3/library/unittest.html
- nose2(Nose): https://docs.nose2.io

