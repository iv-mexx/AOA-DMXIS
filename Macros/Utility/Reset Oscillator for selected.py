#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

ns = GetNumSelCh()
if ns == 0: Message("Select some channels first!")

for i in range(ns):
   ch = GetSelCh(i)
   SetOscType(ch, 0)
   SetOscAmount(ch, 0.5)
   SetOscChase(ch, 0)
   SetOscSpeed(ch, 7)
   SetOscShape(ch, 0.5)

   