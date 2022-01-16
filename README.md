# digital-watermaker

![code check](https://github.com/averak/digital-watermarker/workflows/code%20check/badge.svg)
![Version 1.0](https://img.shields.io/badge/version-1.0-yellow.svg)
![Python 3.6](https://img.shields.io/badge/python-3.9-blue.svg)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

This app is digital watermaker for wave.

## Requirement

- Python 3.9
- pipenv

## Develop

### Installation

```bash
$ pipenv install
```

### Code check & format

```bash
# code check
$ pipenv run lint && pipenv run mypy

# code format
$ pipenv run format
```

## Usage

You can run this application from `src/main.py`.

```bash
# record your voice
$ pipenv run python src/main.py --record

# clear wave data
$ pipenv run python src/main.py --clear
```

Please refer to the help for more detailed usage.

```
$ pipenv run python src/main.py --help
usage: main.py [-h] [-r] [-c]

optional arguments:
  -h, --help    show this help message and exit
  -r, --record  音声を録音
  -c, --clear   音声データを全削除
```
