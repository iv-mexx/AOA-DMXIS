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
        SetOscAmount(ch, 0.5)
        SetOscType(ch, 4)
        SetOscSpeed(ch, 9)
        SetOscChase(ch, 0.0)
        SetOscShape(ch, 0.5)
    elif nm=="tilt":
        SetChVal(ch, 128)
        SetOscAmount(ch, 0.25)
        SetOscType(ch, 3)
        SetOscSpeed(ch, 5)
        SetOscChase(ch, 0.25)
        SetOscShape(ch,0.18)