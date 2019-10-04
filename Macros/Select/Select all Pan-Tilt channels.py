#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

found = False
for ch in GetAllSelCh(True):
    nm = GetChName(ch)
    if nm=="Pan" or nm=="Tilt":
        SelectCh(ch, 1)
        found = True
    else:
        SelectCh(ch, 0)

if not found: Message("No Pan/Tilt channels found!")