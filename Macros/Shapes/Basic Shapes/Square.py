#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

sel = GetAllSelCh(False)
if len(sel)==0: 
    Message("Select some Pan/Tilt channels first!")

for ch in sel:
    nm = GetChName(ch).lower()
    if nm=="pan":
        SetChVal(ch, 128)
        SetOscAmount(ch, 0.25)
        SetOscType(ch, 2)
        SetOscSpeed(ch, 7)
        SetOscChase(ch, 0.0)
        SetOscShape(ch, 0.5)
    elif nm=="tilt":
        SetChVal(ch, 128)
        SetOscAmount(ch, 0.25)
        SetOscType(ch, 2)
        SetOscSpeed(ch, 7)
        SetOscShape(ch, 0.5)
        SetOscChase(ch, 0.25)