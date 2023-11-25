import typer

from .rt import run

app = typer.Typer()

app.command()(run)

app()
