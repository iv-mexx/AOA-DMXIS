#===============================================================
# DMXIS Macro (c) db audioware limited
# David Brown - 10 Feb 2010
#===============================================================
    
#--------------------------------------------------
# Get the user selected channels 
#--------------------------------------------------
sel = GetAllSelCh(False)
if len(sel) < 3: 
   Message("Select at least 3 channels first!")

#--------------------------------------------------
# Get the current range of the first & last channels
# Floating point variables used for better accuracy
#--------------------------------------------------
min = float(GetChVal(sel[0]))
max = float(GetChVal(sel[-1])) # -1 = last selected channel

#--------------------------------------------------
# Increase the outward fan range
#--------------------------------------------------
min = min - 5
if min<0: min=0
max = max + 5
if max>255: max=255

#--------------------------------------------------
# Calculate the spacing between each channel
#--------------------------------------------------
num = float(len(sel))
delta = (float)(max-min)/(num-1.0)

#--------------------------------------------------
# Fan out the channels evenly 
# (leave the first & last channels alone)
#--------------------------------------------------
val = float(min)
for ch in sel:
   SetChVal(ch, int(val))
   val = val + delta