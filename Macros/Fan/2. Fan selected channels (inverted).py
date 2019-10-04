#===============================================================
# DMXIS Macro (c) db audioware limited
# David Brown - 10 Feb 2010
#
# Linear fan.py
# Evenly distributes the selected DMX channels across 
# the range defined by the first & last channel selected.
#===============================================================
    
#--------------------------------------------------
# Get the user selected channels 
#--------------------------------------------------
sel = GetAllSelCh(False)
if len(sel) < 3: 
   Message("Select at least 3 channels first!")

#--------------------------------------------------
# Get the values of the first & last channel
# Floating point variables used for better accuracy
#--------------------------------------------------
min = float(GetChVal(sel[0]))
max = float(GetChVal(sel[-1])) # -1 = last selected channel
if min == max: 
   Message("Adjust the first & last channels\nto set the range of the fan effect!")

#--------------------------------------------------
# Calculate the spacing between each channel
#--------------------------------------------------
num = float(len(sel))
delta = (float)(max-min)/(num-1.0)

#--------------------------------------------------
# Fan out the channels evenly 
# (leave the first & last channels alone)
#--------------------------------------------------
val = float(max)
for ch in sel:
   SetChVal(ch, int(val))
   val = val - delta
SetChVal(sel(0), min)
