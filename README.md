# AOA Live Show

### Channel Patching

Ableton Live can only address 128 Automation Parameters. Minus global Parameters from DMXis, this means that DMX Channel 111 is the last Channel automatable.

With a normal "sane" Placement of Fixtures, the last Fixture would go up to DMX Channel 134 and thus would not be adressable via Ableton Live Automation anymore.

We use Channel Patching to stuff all Fixtures into the first 111 Channels:

* Wild Wash is positioned at Channel 75 between Sunstrips
* Ego Riser LED Bars are placed at 97-106 and 113-122
* Ego-Riser Dimmer and Strobe are patched
  * 29 -> 97 (Master Left)
  * 30 -> 98 (Strobe Left)
  * 31 -> 113 (Master Right)
  * 32 -> 114 (Strobe Right)
* Ego-Riser Colors are patched to be changed together
  * 99-106 -> 99-106
  * 99-106 -> 115-122
  * Effectively, this means that 99-106 control the Colors for both Risers at the same time
