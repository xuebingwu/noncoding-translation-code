#!/usr/bin/python3

import sys
import os
import iupred3_lib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("seqfile", help="FASTA formatted sequence file")
parser.add_argument("iupred_type", help="Analysis type: \"long\", \"short\" or \"glob\"")
parser.add_argument("-a", "--anchor", help="Enable ANCHOR2 prediction",
                    action="store_true")
parser.add_argument("-s", "--smoothing", help="Smoothing type: \"no\", \"medium\" or \"strong\". Default is \"medium\"",
                    default="medium")
# parser.add_argument("-e", "--experimental", help="Filter experimentally verified regions.",
#                     action="store_true")
args = parser.parse_args()

PATH = os.path.dirname(os.path.realpath(__file__))

if args.smoothing not in ['no', 'medium', 'strong']:
    raise ValueError('Smoothing (-s, --smoothing) must be either \"no\", \"medium\" or \"strong\"!')

sequence = iupred3_lib.read_seq(args.seqfile)
with open(args.seqfile,'r') as f:
  for line in f:
    sequence = line.strip()
    iupred2_result = iupred3_lib.iupred(sequence, "short", "no")
    disorder= 0
    for pos, residue in enumerate(sequence):
      disorder = disorder + iupred2_result[0][pos]
    print(sequence+"\t"+str(disorder))

