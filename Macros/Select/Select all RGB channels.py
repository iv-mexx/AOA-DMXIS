#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

found=False
for ch in GetAllSelCh(True):
    nm = GetChName(ch).lower()
    if nm=="r" or nm=="g" or nm=="b" or nm=="red" or nm=="green" or nm=="blue":
        SelectCh(ch, 1)
        found=True
    else:
        SelectCh(ch, 0)
        
if not found: Message("No RGB channels found!")