import click

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo("Initialize the database!")


@cli.command()
def dropdb():
    click.echo("Drop the database!")

if __name__ == '__main__':
    cli()