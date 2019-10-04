#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================
    
sel = GetAllSelCh(False)
if len(sel)>0:
    for ch in sel:
        RemoveFixture(ch)