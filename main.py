""" Command line to use fixup_md_img package """
import argparse
import glob
import os
import sys

from fixup_md_img import fix_md_file


def main():
    """Main function"""

    parser = argparse.ArgumentParser(description="Fix images from markdown files")

    # add arguments for the markdown directory
    parser.add_argument(
        "--md",
        "-m",
        type=str,
        help="The directory containing the markdown files",
        default="./markdown",
        required=True,
    )
    # add argument to force the image directory
    parser.add_argument(
        "--img",
        "-i",
        type=str,
        help="The directory containing the images",
        required=False,
    )

    args = parser.parse_args()
    # if the directory doesn't exist, exit
    if not os.path.isdir(args.md):
        print("The directory {} doesn't exist".format(args.md))
        sys.exit(1)

    # get all markdown files
    mdfiles = glob.glob(os.path.join(args.md, "*.md"))

    # fix each markdown file
    for mdfile in mdfiles:
        print(f"Fixing {mdfile}")
        content = ""
        with open(mdfile, "r") as mdfp:
            content += mdfp.read()
        # fix the markdown file and image extension
        new_content = fix_md_file(content, mdfile, args.img if args.img else None)
        with open(mdfile, "w") as mdfp:
            mdfp.write(new_content)


if __name__ == "__main__":
    main()
