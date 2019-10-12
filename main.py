#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json
from diaa.maker import *
import operator

if __name__ == "__main__":
    pparser = argparse.ArgumentParser()
    #pparser.add_argument('-a', nargs='+', help='annotators', required=False, default=[])
    pparser.add_argument('-i', help='input', required=False )
    #pparser.add_argument('-d', help='docs', action='store_true', required=False, )
    pparser.add_argument('-u', help='url', nargs='+', default=[], required=False, )
    #pparser.add_argument('-p', help='project', required=False, )


    args = pparser.parse_args()

    if args.u :
        docs = get_docs_from_doccano(args.u)
    else:
        docs = get_docs_from_json(args.i)

    # if args.d:
    #     doc_agree={}
    #     for i in range(len(docs)):
    #         doc=docs[i]
    #         labels=get_labels([doc])
    #         ag=calc(labels)
    #         doc_agree[i]=ag["kappa"]
    #
    #     sorted_agreeemnt = sorted(doc_agree.items(), key=operator.itemgetter(1))
    #     print (sorted_agreeemnt)
    # else:

    labels=get_labels(docs)
    compute_f1_scores(docs)

    agreement=calc(labels)
    print (agreement)


    #docs_to_ann(docs)





