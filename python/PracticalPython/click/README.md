# What is the Click?
 - Command Line Interface Creation Kit

## Features:
- Arbitrary nesting of commands
- Automatic help page generation
- Aupports lazy loading of subcommands at runtime

### Basic concept
```python
import click
@click.command()
def hello():
    click.echo('Hello World!')
```

- The function becomes a Command line tool by decorating it with `@click.command()`
- Instead of using print we use to `@click.echo` to support in different environment consistently. 
- example: [basic.py](basic.py)

### Grouping
- using Group to grouping the modules
    - group can be called by `@click.group()`
- add submodules to the group module.
    - decorate with `@group_name.command()`
    - `@group_name.add_command(submodule)`
- example: [group.py](group.py)

### Adding Paramenters
- `@click.option`: Option parameter, support default and help message.
- `@click.argument`: The argument which must be required.
- example: [add_params.py](add_params.py)

### Setuptools Integration
- Add [setup.py](setup.py) from the top of the package.

```
project/
    yourpackage/
        __init__.py
        main.py
        utils.py
        scripts/
            __init__.py
            yourscript.py
    setup.py
```

- Edit the setup.py
```python
from setuptools import setup, find_packages

setup(
    name='yourpackage',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'yourscript = yourpackage.scripts.yourscript:cli',
        ],
    },
)
```

## Reference: 
- https://click.palletsprojects.com/en/8.0.x/