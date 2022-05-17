# 📖 Readtime-CLI

CLI to calculates the time some text takes the average human to read, based on Medium's [read time forumula](https://help.medium.com/hc/en-us/articles/214991667-Read-time).


## 🧮 Algorithm

Medium's Help Center says,

> Read time is based on the average reading speed of an adult (roughly 265 WPM). We take the total word count of a post and translate it into minutes, with an adjustment made for images. For posts in Chinese, Japanese and Korean, it's a function of number of characters (500 characters/min) with an adjustment made for images.

[Source](https://help.medium.com/hc/en-us/articles/214991667-Read-time)

Double checking with real articles, the English algorithm is:

    seconds = num_words / 265 * 60 + img_weight * num_images

With `img_weight` starting at `12` and decreasing one second with each image encountered, with a minium `img_weight` of `3` seconds.


## Requirements

Python 3.9+

Readtime-CLI stands on the shouders of giants:

* [Typer](https://github.com/tiangolo/typer)
* [Readtime](https://github.com/alanhamlett/readtime)


## 🛠 Installation

### Poetry

    poetry add readtime_cli

### Pip

    virtualenv venv
    . venv/bin/activate
    pip install readtime_cli


## 💻 Usage


### Version

    ```sh
    readtime version
    ```

### Calculate Read time Markdown files

    ```sh
    readtime md FILE_PATH [OPTIONS]
    ```

### Calculate Read time HTML files

    ```sh
    readtime html FILE_PATH [OPTIONS]
    ```

### Calculate Read time Text files

    ```sh
    readtime text FILE_PATH [OPTIONS]
    ```

### Options for all commands

    --wpm INTEGER  Word Per Minute  [default: 265]
    --help         Show help and exit.