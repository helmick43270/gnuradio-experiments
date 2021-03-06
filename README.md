# gnuradio-experiments 
The dot-grc file is a flowgraph meant to be loaded by Gnu Radio Companion. This module receives audio from the default microphone and removes a sideband in the complex frequency domain. This is part of an attempt to fit a HackRF clone into a software-defined single sideband amateur radio satellite uplink system.  \
The Hilbert Transform (absolutely no idea how it works) seems to perform better with a Hann (cosine) window rather than with a default Hamming (triangle) window with respect to carrier suppression. The dot-py code can be run without Gnu Radio Companion, but I think Gnu Radio has to be installed. \
I ran this flowgraph on a HackRF clone with a 50-ohm dummy load on the antenna output, and had another computer running gqrx with a DVB-T dongle with an antenna about 2 feet away that could pick up my voice.
![flowgraph](https://user-images.githubusercontent.com/67888072/147993436-d0e66329-609a-4947-9edc-1932a7a3e177.png)
