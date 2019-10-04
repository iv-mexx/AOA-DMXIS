#===============================================================
# DMXIS Macro (c) db audioware limited
#===============================================================
    
sel = GetAllSelCh(False)
if len(sel) < 1: 
   Message("Select at least 1 channel first!")
for ch in sel:
   SetChEnabled(ch, 0)