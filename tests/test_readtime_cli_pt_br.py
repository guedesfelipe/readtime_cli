from typer.testing import CliRunner

from readtime_cli.main import app

runner = CliRunner()
LANGUAGE = 'pt-br'


def test_html():
    result = runner.invoke(
        app, ['html', 'tests/fixtures/html_file.html', '--language', LANGUAGE]
    )
    assert result.exit_code == 0
    assert result.stdout == '18 min leitura\n'


def test_md():
    result = runner.invoke(
        app, ['md', 'tests/fixtures/markdown_file.md', '--language', LANGUAGE]
    )
    assert result.exit_code == 0
    assert result.stdout == '2 min leitura\n'


def test_text():
    result = runner.invoke(
        app, ['text', 'tests/fixtures/text_file.txt', '--language', LANGUAGE]
    )
    assert result.exit_code == 0
    assert result.stdout == '1 min leitura\n'


def test_html_wpm_100():
    result = runner.invoke(
        app,
        [
            'html',
            'tests/fixtures/html_file.html',
            '--wpm',
            '100',
            '--language',
            LANGUAGE,
        ],
    )
    assert result.exit_code == 0
    assert result.stdout == '46 min leitura\n'


def test_md_wpm_100():
    result = runner.invoke(
        app,
        [
            'md',
            'tests/fixtures/markdown_file.md',
            '--wpm',
            '100',
            '--language',
            LANGUAGE,
        ],
    )
    assert result.exit_code == 0
    assert result.stdout == '3 min leitura\n'


def test_text_wpm_100():
    result = runner.invoke(
        app,
        [
            'text',
            'tests/fixtures/text_file.txt',
            '--wpm',
            '100',
            '--language',
            LANGUAGE,
        ],
    )
    assert result.exit_code == 0
    assert result.stdout == '2 min leitura\n'
