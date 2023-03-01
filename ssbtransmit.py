#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ssbtransmit
# Author: helmick
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import audio
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import osmosdr
import time
from gnuradio import qtgui

class ssbtransmit(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ssbtransmit")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ssbtransmit")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ssbtransmit")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.transmit_freq = transmit_freq = 144190000
        self.samp_rate = samp_rate = 32000
        self.rfsamp = rfsamp = 2400000
        self.finetune = finetune = 0

        ##################################################
        # Blocks
        ##################################################
        self._transmit_freq_range = Range(144100000, 144400000, 500, 144190000, 200)
        self._transmit_freq_win = RangeWidget(self._transmit_freq_range, self.set_transmit_freq, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._transmit_freq_win)
        self._finetune_range = Range(-300, 300, 1, 0, 200)
        self._finetune_win = RangeWidget(self._finetune_range, self.set_finetune, 'Clarify', "counter_slider", float)
        self.top_grid_layout.addWidget(self._finetune_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(rfsamp/samp_rate),
                decimation=1,
                taps=None,
                fractional_bw=None)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "device='HackRF',driver=hackrf,part_id=a000cb3c005f4f5f,serial=0000000000000000644064dc367c9dcd,soapy=3,version=2018.01.1"
        )
        self.osmosdr_sink_0.set_sample_rate(rfsamp)
        self.osmosdr_sink_0.set_center_freq(transmit_freq+finetune, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.hilbert_fc_0 = filter.hilbert_fc(4000, firdes.WIN_HANN, 6.76)
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                2.4,
                samp_rate,
                400,
                2400,
                20,
                firdes.WIN_HANN,
                6.76))
        self.audio_source_0 = audio.source(samp_rate, '', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.osmosdr_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ssbtransmit")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_transmit_freq(self):
        return self.transmit_freq

    def set_transmit_freq(self, transmit_freq):
        self.transmit_freq = transmit_freq
        self.osmosdr_sink_0.set_center_freq(self.transmit_freq+self.finetune, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(2.4, self.samp_rate, 400, 2400, 20, firdes.WIN_HANN, 6.76))

    def get_rfsamp(self):
        return self.rfsamp

    def set_rfsamp(self, rfsamp):
        self.rfsamp = rfsamp
        self.osmosdr_sink_0.set_sample_rate(self.rfsamp)

    def get_finetune(self):
        return self.finetune

    def set_finetune(self, finetune):
        self.finetune = finetune
        self.osmosdr_sink_0.set_center_freq(self.transmit_freq+self.finetune, 0)



def main(top_block_cls=ssbtransmit, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
