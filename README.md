# Fix image in Markdown directory

Ths script fixes markdown file and image in a given directory.
- it detects the image format to fix the extension (if possible)
- if the image is correcty renames, the path is changed in markdown

**Before testing, BACKUP YOUR CONTENT**

## Installation

Using of `poetry` is recommended:

```bash
poetry install

# check
poetry run python main.py -h
```

Or use virtual env and install dependencies with "pip":

```bash
python -mvenv ./.venv
source .venv/bin/activate

# install needed dependencies
pip install Pillow

# check
python main.py -h
```

You can, of course, use globally installed Python but you need to install `Pillow` package.

## Usage

The required argument is `-m` or `--md` that should be set to a path where the script can find markdown files.

If the images are placed somewhere else (e.g. `![](../images)` and "images" directory is **not** placed one directory up from the markdown files) so you can force the image directory path with `-i` or `--img` argument.

```bash
python main.py -m ./markdown
python main.py -m ./markdown -i outside/images
```
