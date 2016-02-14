#!/usr/bin/env python

import sys
import os.path
import csv

##################################################
#~ MAIN !
##################################################
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: {} <faces_dir> <out_csv_filename>".format(sys.argv[0]))
        sys.exit(1)

    facesdir = sys.argv[1]
    outfilename = sys.argv[2]
    id_ = 0

    with open(outfilename, 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=['path','id'])
        csvwriter.writeheader()
        for dirpath, dirnames, filenames in os.walk(facesdir):
            for f in filenames:
                if f.endswith(".pgm"):
                    path = os.path.abspath(os.path.join(dirpath, f))
                    csvwriter.writerow({'path':path, 'id':id_})
            id_ += 1
