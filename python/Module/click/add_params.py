"""
Basic example of adding parmeters in click.
"""
import click

@click.command()
@click.option('--count', default = 1, help='Number of times to print')
@click.argument('name')
def say_hello(count, name):
    """
    Print number of times names.
    """
    for _ in range(count):
        click.echo(f'Hello, {name}')

if __name__ == '__main__':
    say_hello()