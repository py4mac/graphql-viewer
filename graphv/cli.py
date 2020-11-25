import click
from graphv.version import VERSION
from graphv.api import serve_application


@click.group()
@click.version_option(VERSION)
def cli():
    pass


@cli.command()
def run():
    serve_application()


if __name__ == "__main__":
    cli()
