#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

import sys

import _DmxApi
from _DmxApi import *

print("Initialising general helpers...")

def GetAllSelCh(doAll):
    ns = GetNumSelCh()
    if ns==0 and doAll: return range(512)
    sc = []
    for i in range(ns):
        sc.append(GetSelCh(i))
    return sc