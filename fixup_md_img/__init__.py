""" Fix images from markdown files """
__version__ = "0.1.0"
import mimetypes
import os
import re

from PIL import Image

IMG_REG = re.compile(r"!\[(.*?)\]\((.*?)\)")


def get_extension(i):
    """Get the extension of an image"""
    return mimetypes.guess_extension(i.get_format_mimetype())


def fix_md_file(mdcontent, mdpath, imagedir=None, dry_run=False) -> str:
    """Get all images from a markdown file
    Then replace the image filename with the right extension
    """

    # get the markdown path
    new_content = []
    replacements = {}
    for line in mdcontent.split("\n"):
        # remove the newline
        line = line.rstrip()
        # find images
        imgs = IMG_REG.findall(line)
        images = []
        if imgs:
            for img in imgs:
                images.append(img[1])
        # replace image filename with extension
        for image in images:
            if imagedir is not None:
                impath = os.path.join(imagedir, image)
            else:
                impath = os.path.join(os.path.dirname(mdpath), image)

            impath = os.path.realpath(impath)
            try:
                ext = get_extension(Image.open(impath))
            except FileNotFoundError:
                print(f"{impath} not found")
                continue
            if ext is None:
                print(f"Could not find extension for {image}")
                continue

            origin = image
            if image[-1] == ".":
                image = image[:-1]
            if image in replacements:
                continue
            if ext != image[-4:]:
                replacements[image] = image + ext
                print(f"{origin} -> {replacements[image]}")
            else:
                print(f"{origin} already has the right extension")
                continue

            # copy the file to the right extension
            if not dry_run:
                os.rename(
                    impath,
                    os.path.join(
                        os.path.dirname(impath), os.path.basename(replacements[image])
                    ),
                )

        # replace the image filename with the right extension in the line
        for imagename, fixed in replacements.items():
            line = line.replace(imagename, fixed)
        new_content.append(line)
    return "\n".join(new_content)
