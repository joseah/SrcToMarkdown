
# Src2Markdown

# Description

`SrctoMarkdown.py` takes a script written in **python**, **perl**, **javascript**, **R** or **shell**
and generates a markdown document with comments processed as markdown text, and code embedded in
markdown code tags.

The output file is then converted into html, pdf, and other output formats supported by `Pandoc`.


# Requirements

## Pandoc

This program requires [Pandoc](http://pandoc.org/) to convert the markdown output generated
with this program to any other format.

Download Pandoc from the [installing webpage](http://pandoc.org/installing.html). 

## pypandoc

In order to use pandoc within python, pypandoc wrapper is required.

Install `pypandoc` via `pip`:

```bash
sudo pip install pypandoc
```

> See [pip webpage](https://pip.pypa.io/en/stable/installing/) if you do not use `pip` yet


# Parameter description


| Parameters |                  Description                   | Mandatory? |
|:----------:|:----------------------------------------------:|:----------:|
| -s         | script file (with comments in markdown style)  |Yes         |
| -o         |      output format (html, pdf, rst, ...)       |Yes         |
| -c         |                    css file                    |No          |
| -md        |            Write markdown output?              |No          |
| -pandoc    |Path to pandoc. Default `/usr/local/bin/pandoc` |No          |

# Usage example

```shell
python SrctoMarkdown.py -s functions.js -o html -c kult.css
```

Creates an html report for `functions.js`. A CSS file is used to give style to html output file.


# Notes

This program is humbly inspired by the awesome work on Knitr by **Yihui Xie** and Rmarkdown by **JJ Allaire**.

# Contributors

- José Alquicira Hernández
