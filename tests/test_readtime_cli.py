from typer.testing import CliRunner

from readtime_cli import __version__
from readtime_cli.main import app

runner = CliRunner()


def test_version():
    assert __version__ == '0.1.0'


def test_error():
    result = runner.invoke(app, ['test', '--city', 'Berlin'])
    assert result.exit_code == 2
    assert "Error: No such command 'test'" in result.stdout


def test_error_2():
    result = runner.invoke(app, ['text', '../poetry.lock', '--city', 'Berlin'])
    assert result.exit_code == 2
    assert 'Error: No such option: --city' in result.stdout


def test_help():
    result = runner.invoke(app, ['--help'])
    assert result.exit_code == 0
    assert 'Commands:\n  html\n  md\n  text\n  version\n' in result.stdout


def test_version_command():
    result = runner.invoke(app, ['version'])
    assert result.exit_code == 0
    assert result.stdout == f'Readtime CLI Version: {__version__}\n'


def test_html():
    result = runner.invoke(app, ['html', 'tests/fixtures/html_file.html'])
    assert result.exit_code == 0
    assert result.stdout == '18 min read\n'


def test_md():
    result = runner.invoke(app, ['md', 'tests/fixtures/markdown_file.md'])
    assert result.exit_code == 0
    assert result.stdout == '2 min read\n'


def test_text():
    result = runner.invoke(app, ['text', 'tests/fixtures/text_file.txt'])
    assert result.exit_code == 0
    assert result.stdout == '1 min read\n'


def test_html_wpm_100():
    result = runner.invoke(
        app, ['html', 'tests/fixtures/html_file.html', '--wpm', '100']
    )
    assert result.exit_code == 0
    assert result.stdout == '46 min read\n'


def test_md_wpm_100():
    result = runner.invoke(
        app, ['md', 'tests/fixtures/markdown_file.md', '--wpm', '100']
    )
    assert result.exit_code == 0
    assert result.stdout == '3 min read\n'


def test_text_wpm_100():
    result = runner.invoke(
        app, ['text', 'tests/fixtures/text_file.txt', '--wpm', '100']
    )
    assert result.exit_code == 0
    assert result.stdout == '2 min read\n'
