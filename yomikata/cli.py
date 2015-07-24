# -*- coding: utf-8 -*-
import sys

from . import Yomikata


def main():
    if len(sys.argv) != 2:
        Yomikata()
    arg = sys.argv[1]
    Yomikata(arg)
