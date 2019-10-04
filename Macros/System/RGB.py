#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

import sys

import _DmxApi
from _DmxApi import *

import System.Helpers
from System.Helpers import *

print("Initialising RGB helpers...")

def RgbColour(r,g,b):
    sel = GetAllSelCh(False)
    if len(sel)==0: 
        Message("Select some RGB channels first!")

    for ch in sel:
        nm = GetChName(ch).lower()
        if nm=="r" or nm=="red":
            SetChVal(ch, r)
        elif nm=="g" or nm=="green":
            SetChVal(ch, g)
        elif nm=="b" or nm=="blue":
            SetChVal(ch, b)