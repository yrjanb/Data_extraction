#this file is a direct copy from https://github.com/PacktPublishing/Python-Digital-Forensics/blob/master/Section%202/directory_scan.py
#All credit goes to kd8bny (Daryl Bennet)
import os
import argparse


class DirectoryWalk:
    def __init__(self):
        """Here we set the global defaults"""
        self.path = ''

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Scan all magic files")
        parser.add_argument("path", help="Path to folder")

        return parser.parse_args()

    def scan_path(self):
        with os.scandir(self.path) as iter_path:
            for entry in iter_path:
                print(entry.name)

    def main(self):
        args = self.get_args()
        self.path = args.path

        self.scan_path()


if __name__ == '__main__':
    walk_instance = DirectoryWalk()
    walk_instance.main()
