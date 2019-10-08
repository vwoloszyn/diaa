#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json
from diaa.maker import *


if __name__ == "__main__":
    pparser = argparse.ArgumentParser()
    #pparser.add_argument('-a', nargs='+', help='annotators', required=False, default=[])
    pparser.add_argument('-a', help='annotators', required=True, )


    args = pparser.parse_args()

    if args.a:
        calc(args.a)

