# AOA Live Show

### Channel Patching

#### Ableton Live Automation Limitation

Ableton Live can only address 128 Automation Parameters. Minus global Parameters from DMXis, this means that DMX Channel 111 is the last Channel automatable.

With a normal "sane" Placement of Fixtures, the last Fixture would go up to DMX Channel 134 and thus would not be adressable via Ableton Live Automation anymore.

We use Channel Patching to stuff all Fixtures into the first 111 Channels.

#### Controlling multiple fixtures at once

The second use for channel patching is to controll multiple channels with the same faders in DMXIS, e.g. 

* Colors Ego Risers & Drums 
* Dimmers and Strobes for Ego Risers (which now have multiple fixtures inside)


#### Patching Table

* LED Matrix Top: 1:28 -> 1:28
* LED Matrix Bottom: 33:62 -> 33:62
* Sunstrip L
  * 65:74 -> 65:74
* Sunstrip R
  * 81:90 -> 81:90
* Ego Riser L
  * 29:30 (Dimmer, Strobe) -> 97:98 (Eurolite LED BAR-3 HCL Bar)
  * 29:30 (Dimmer, Strobe) -> 146:147 (Varytec Giga Bar HEX 3)
  * 99:106 (RGBAWUV - Primary Color) -> 99:106 (Eurolite LED BAR-3 HCL Bar)
  * 99:104 (RGBAWUV - Primary Color) -> 140:145 (Varytec Giga Bar HEX 3)
* Ego Riser R
  * 31:32 (Dimmer, Strobe) -> 113:114 (Eurolite LED Bar-3 HCL Bar)
  * 31:32 (Dimmer, Strobe) -> 156:157 (Varytec Giga Bar HEX 3)
  * 99:106 (RGBAWUV - Primary Color) -> 115:122 (Eurolite LED BAR-3 HCL Bar)
  * 99:104 (RGBAWUV - Primary Color) -> 150:155 (Varytec Giga Bar HEX 3)
* Drums
  * 75:76 (Dimmer, Strobe) -> 129:130 (Eurolite LED Bar-3 HCL Bar)
  * 75:76 (Dimmer, Strobe) -> 166:167 (Varytec Giga Bar HEX 3, Primary Color)
  * 75:76 (Dimmer, Strobe) -> 176:177 (Varytec Giga Bar HEX 3, Complementary Color)
  * 99:106 (RGBAWUV - Primary Color) -> 131:138 (Eurolite LED BAR-3 HCL Bar) 
  * 99:104 (RGBAWUV - Primary Color) -> 160:165 (Varytec Giga Bar HEX 3, Primary Colo)
  * 107:112 (RGBAWUV - Complementary Color) -> 170:175 (Varytec Giga Bar HEX 3, Complementary Color)
* Fog Machines (All)
  * 64 -> 64