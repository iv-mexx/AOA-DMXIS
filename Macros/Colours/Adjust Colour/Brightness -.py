#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

for ch in GetAllSelCh(False):
    nm = GetChName(ch).lower()
    if nm=="r" or nm=="red" or nm=="g" or nm=="green" or nm=="b" or nm=="blue":
        v = GetChVal(ch) - 5
        if (v>255): v=255
        SetChVal(ch, v)
        
