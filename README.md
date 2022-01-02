# gnuradio-experiments 
The .grc file is a flowgraph meant to be loaded by Gnu Radio Companion. This module receives audio from the default microphone and removes a sideband in the complex frequency domain (please excuse any misused technical terms the author has not yet fully comprehended.) This is part of an attempt to fit a HackRF clone into a software-defined single sideband amateur radio satellite uplink system. 
The Hilbert Transform (absolutely no idea how it works) seems to perform better with a Hann (cosine) window rather than with a default Hamming (triangle) window.
![flowgraph](https://user-images.githubusercontent.com/67888072/147885756-c7afa7b2-cba5-491a-905c-2a9002b6229a.png)
