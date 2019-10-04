#===============================================================
# DMXIS Macro (c) 2011 db audioware limited
#===============================================================

#----------------------------------
# Get the selected channels
#----------------------------------
sel = GetAllSelCh(False)
if len(sel)==0: 
    Message("Select some channels first!")

#----------------------------------
# Find the number of selected fixtures
#----------------------------------
numSelFix = 0;
firstChName = GetChName(sel[0]).lower()
for ch in sel:
   nm = GetChName(ch).lower()
   if nm==firstChName: 
      numSelFix += 1

#----------------------------------
# Error if multiple fixtures not selected
#----------------------------------
if numSelFix<2:
   Message("Select the same channels on >1 fixture!")

#----------------------------------
# Chase these channels across all selected fixtures
#----------------------------------
delta = 1.0/float(numSelFix)	phase = 0for ch in sel:   nm = GetChName(ch).lower()
   if nm==firstChName and ch!=sel[0]:
      phase += delta

   v = GetChVal(ch)
   vf = float(v)
   amt = vf/255.0
   SetChVal(ch, v/2)
   SetOscAmount(ch, vf/512.0)
   SetOscType(ch, 2)
   SetOscSpeed(ch, 7)
   SetOscChase(ch, phase)
   SetOscShape(ch, 0.5)
