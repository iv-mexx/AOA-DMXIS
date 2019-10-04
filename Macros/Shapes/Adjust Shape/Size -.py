#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

sel = GetAllSelCh(False)
if len(sel)==0: 
    Message("Select some Pan/Tilt channels first!")

for ch in sel:
    nm = GetChName(ch).lower()
    if nm=="pan" or nm=="tilt":
        cv = GetOscAmount(ch);
        cv -= 0.02
        SetOscAmount(ch, cv)