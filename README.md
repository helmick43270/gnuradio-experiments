# gnuradio-experiments 
The dot-grc file is a flowgraph meant to be loaded by Gnu Radio Companion. This module receives audio from the default microphone and removes a sideband in the complex frequency domain. This is part of an attempt to fit a HackRF clone into a software-defined single sideband amateur radio satellite uplink system.  \
The Hilbert Transform (absolutely no idea how it works) seems to perform better with a Hann (cosine) window rather than with a default Hamming (triangle) window with respect to carrier suppression. The dot-py code can be run without Gnu Radio Companion, but I think Gnu Radio has to be installed. \
I ran this flowgraph on a HackRF clone with a 50-ohm dummy load on the antenna output, and had another computer running GQRX with a DVB-T dongle with an antenna about 2 feet away that could pick up my voice. \
![flowgraph](https://user-images.githubusercontent.com/67888072/147993436-d0e66329-609a-4947-9edc-1932a7a3e177.png)
On 11/29/2022, I used a flowgraph very similar to this with my HackRF, a preamp, and a QRP final amp, and was heard on the Tuesday night 2m vertical SSB net on 144.19MHz. I used a 2m filter, a Pico Macom CATV 30dB headend preamp, and a cheap DVB-T dongle with Alexandru Csete's GQRX app on another laptop to listen. I switched the antenna between receive and transmit lines and shut down the CATV preamp while transmitting. My antenna system is a 2m cavity (to reduce out-of-band products and receive preamp overloading), 80 feet of RG8X feed line, and a homebrew 2m 5/8 wave ground plane at around 35 feet high. That was the result of around two years of tinkering and several years of thinking, hobby-style. Since then, I have checked in to that net a couple more times, and have been heard clearly from 50 miles away. \
The ssbtransmit and ssbreceive flowgraphs are my more lightweight and purpose-driven improvements based on some others' work and some of my own reinventions while remaining in the relative comfort of Gnu Radio Companion. \
Watch Michael Ossman's HackRF lessons on Youtube!
