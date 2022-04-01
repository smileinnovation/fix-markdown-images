import os

from fixup_md_img import __version__, fix_md_file, get_extension
from PIL import Image


def test_version():
    assert __version__ == "0.1.0"


def test_get_ext():
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data/images/profile"
    )
    image = Image.open(file)
    assert get_extension(image) == ".jpg"


def test_fixing():
    content = """# A title
This is a file with ![](../images/profile) image. And another one: ![](../images/profile) -- OK ?
One more line: ![](../images/profile)
    """
    expected = """# A title
This is a file with ![](../images/profile.jpg) image. And another one: ![](../images/profile.jpg) -- OK ?
One more line: ![](../images/profile.jpg)
"""
    assert fix_md_file(content, "tests/data/markdowns/FOO.md", dry_run=True) == expected
