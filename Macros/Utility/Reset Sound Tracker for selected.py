#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

ns = GetNumSelCh()
if ns == 0: Message("Select some channels first!")

for i in range(ns):
   ch = GetSelCh(i)
   SetStLevel(ch, 0)
   SetStBand(ch, 0)
   SetStAttack(ch, 0)
   SetStRelease(ch, 0)
   SetStDir(ch, 0)