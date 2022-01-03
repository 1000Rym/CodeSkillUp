from setuptools import setup

setup(
    name='add_params',
    version='0.1.0',
    py_modules=['cli_test_add_params'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'add_params = add_params:say_hello',
        ],
    },
)