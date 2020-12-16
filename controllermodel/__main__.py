import argparse
import os
import importlib
import pathlib

from .gendoc import GenDoc

if __name__ == '__main__':
    # print("ControllerModel Model Controller control version 1.2.8.4.3.19.rc4.beta3.prerelease7-6rc2")
    # parser = argparse.ArgumentParser(description='Open a python application or file and generate documentation')
    # parser.add_argument('file', metavar='F', type=str, nargs="+", help="The file(s) to process documentation for")
    # parser.add_argument('-o, --outputdir', metavar='O', type=str, default=os.getcwd(), help="The optional output directory to output documentation to")
    # parser.add_argument('-s, --seperate', action='store_const', const=True, default=False, help="Output all controllers to their own documentation file")
    # args = parser.parse_args()
    # print(args)
    # target_module_path = pathlib.Path(str(args.file[0]))
    # print(target_module_path.absolute())
    # target_module = importlib.import_module(str(target_module_path.absolute()), str(target_module_path.absolute()))
    # print(target_module)
    # gd = GenDoc()
    print("This library does not include any runnable modules.")
    exit(1)