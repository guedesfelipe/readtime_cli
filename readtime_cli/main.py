import readtime
import typer

from readtime_cli import __version__

app = typer.Typer()


@app.command()
def version():
    typer.echo(f'Readtime CLI Version: {__version__}')
    raise typer.Exit()


@app.command()
def text(file: typer.FileText = typer.Argument(...)):
    typer.echo(readtime.of_text(''.join(file.readlines())))


@app.command()
def md(file: typer.FileText = typer.Argument(...)):
    typer.echo(readtime.of_markdown(''.join(file.readlines())))


@app.command()
def html(file: typer.FileText = typer.Argument(...)):
    typer.echo(readtime.of_html(''.join(file.readlines())))
