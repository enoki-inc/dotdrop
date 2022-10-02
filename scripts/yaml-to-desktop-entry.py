#!/usr/bin/env python3
"""
generate .desktop file from inputs in dotdrop config.yaml file
usage example:
    ./yaml-to-desktop-entry.py --version 1.0 --name Chrome --type Application --terminal true --exec flatpak run com.google.Chrome --nodisplay false --genericname Web Browser --outpath ~/.local/share/applications/chrome.desktop
"""

import os
import io
from docopt import docopt
from ruamel.yaml import YAML as yaml

USAGE = """
yaml-to-desktop-entry.py

Usage:
  yaml-to-desktop-entry.py --version=<version> --name=<name> --entrytype=<type> --terminal=<terminal> --execute=<execute> --nodisplay=<nodisplay> --genericname=<genericname> --outpath=<outpath>
  yaml-to-desktop-entry.py --help

Options:
  -h --help               Show this screen.

"""

def main():
    """entry point"""
    args = docopt(USAGE)
    #path = os.path.expanduser(args['<config.yaml>'])
    version = args['--version']
    name = args['--name']
    entrytype = args['--entrytype']
    terminal = args['--terminal']
    execute = args['--execute']
    nodisplay = args['--nodisplay']
    genericname = args['--genericname']
    output_path = args['--outpath']

    with open(output_path, 'w') as file:
        file.write('[Desktop Entry]\n')
        file.write('Version=' + str(version) + '\n')
        file.write('Name=' + str(name) + '\n')
        file.write('Type=' + str(entrytype) + '\n')
        file.write('Terminal=' + str(terminal) + '\n')
        file.write('Exec=' + str(execute) + '\n')
        file.write('NoDisplay=' + str(nodisplay) + '\n')
        file.write('GenericName=' + str(genericname))
        
        file.close()

if __name__ == '__main__':
    main()
