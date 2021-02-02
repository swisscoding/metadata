#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from PIL import Image
from PIL.ExifTags import TAGS

# decoration
print(stylize("\n---- | Extract metadata from image | ----\n", fg("red")))

# class
class Metadata:
    def __init__(self, file):
        self.file = file

    # output magic method
    def __repr__(self):
        metadata = self.extract_metadata(self.file)
        if len(metadata) == 0:
            return stylize(f"\n{self.file} has no metadata.\n", fg("red"))
        else:
            print(stylize(f"\nMetadata of {self.file}:\n", fg("red")))
            for data in metadata:
                print(data)
            return ""

    # methods
    def extract_metadata(self, file):
        # open image
        image = Image.open(file)

        # get metadata
        exifdata = image.getexif()

        # list of metadata
        metadata = []

        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)

            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()

            metadata.append(f"{tag:25}: {data}")

        return metadata

# main execution
if __name__ == "__main__":
    # user interaction
    filename = input("Filename: ")

    print(Metadata(filename))
