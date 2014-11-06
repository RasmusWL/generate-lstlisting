#!/usr/bin/env python3

import outputter, argumentparser
import sys, os
from classes import *

version = "0.1.0"
debug = False

def main():
    (indir) = argumentparser.parse_cli()

    out_file = open(settings.outfile, "w")

    outputter.output_start(out_file)

    relStart = os.path.basename(os.path.abspath(indir))
    files = []
    fil = indir
    relName = relStart

    while fil is not None:
        if os.path.isdir(fil):
            new = list( map (lambda x: (os.path.join(fil+"/", x), relName+"/"+x), os.listdir(fil) ) )
            new.sort()
            files = new + files
        else:
            outputter.output(fil, relName, out_file)

        if files:
            (fil, relName) = files.pop(0)
        else:
            fil = None

    out_file.close()


if __name__ == "__main__":
    realException = None
    try:
        main()
    except KeyboardInterrupt:
        print ("Thank you, come again!")
