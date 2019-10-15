#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json
from diaa.maker import *
import operator
import bratiaa as biaa

if __name__ == "__main__":
    pparser = argparse.ArgumentParser()
    pparser.add_argument('-i', help='input', required=False )
    pparser.add_argument('-u', help='url', nargs='+', default=[], required=False, )
    args = pparser.parse_args()

    if args.u :
        docs = get_docs_from_doccano(args.u)
    else:
        docs = get_docs_from_json(args.i)

    labels=get_labels(docs)
    agg=compute_f1_scores(docs)
    biaa.iaa_report(agg)
    agreement=calc(labels)
    print (agreement)






