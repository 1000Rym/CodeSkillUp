"""
Basic Example of the Click.
"""
import click

@click.command()
def hello():
    click.echo("Hello my world!")

if __name__ == '__main__':
    hello()
    