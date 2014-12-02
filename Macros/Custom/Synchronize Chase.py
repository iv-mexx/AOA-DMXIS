#===============================================================

# DMXIS Macro (c) 2011 db audioware limited
#===============================================================


#----------------------------------
# Get the selected channels
#----------------------------------
n = GetNumSelCh()
for i in range(n):
   ch = GetSelCh(i)

   SetChVal(ch, GetChVal(ch))
   SetOscAmount(ch, GetOscAmount(ch))
   SetOscType(ch, GetOscType(ch))
   SetOscSpeed(ch, GetOscSpeed(ch))
   SetOscChase(ch, GetOscChase(ch))
   SetOscShape(ch, GetOscShape(ch))
