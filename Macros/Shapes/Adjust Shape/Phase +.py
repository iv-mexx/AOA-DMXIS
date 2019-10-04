#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

sel = GetAllSelCh(False)
if len(sel)==0: 
    Message("Select some Pan/Tilt channels first!")

for ch in sel:
    nm = GetChName(ch).lower()
    if nm=="pan" or nm=="tilt":
        v = GetOscChase(ch);
        v += 0.05
        if v>1.0: v = v-1.0
        SetOscChase(ch, v)