
import math
import os
import unittest
from scipy.stats import binned_statistic_2d
import numpy as np

import sas.sascalc.dataloader.data_info as data_info
from sas.sascalc.dataloader.loader import Loader
from sas.sascalc.dataloader.manipulations import (Boxavg, Boxsum,
                                                  CircularAverage, Ring,
                                                  SectorPhi, SectorQ, SlabX,
                                                  SlabY, get_q,
                                                  reader2D_converter)


def find(filename):
    return os.path.join(os.path.dirname(__file__), 'data', filename)


class Averaging(unittest.TestCase):
    """
        Test averaging manipulations on a flat distribution
    """

    def setUp(self):
        """
            Create a flat 2D distribution. All averaging results
            should return the predefined height of the distribution (1.0).
        """
        x_0 = np.ones([100, 100])
        dx_0 = np.ones([100, 100])

        self.data = data_info.Data2D(data=x_0, err_data=dx_0)
        detector = data_info.Detector()
        detector.distance = 1000.0  # mm
        detector.pixel_size.x = 1.0  # mm
        detector.pixel_size.y = 1.0  # mm

        # center in pixel position = (len(x_0)-1)/2
        detector.beam_center.x = (len(x_0) - 1) / 2  # pixel number
        detector.beam_center.y = (len(x_0) - 1) / 2  # pixel number
        self.data.detector.append(detector)

        source = data_info.Source()
        source.wavelength = 10.0  # A
        self.data.source = source

        # get_q(dx, dy, det_dist, wavelength) where units are mm,mm,mm,and A
        # respectively.
        self.qmin = get_q(1.0, 1.0, detector.distance, source.wavelength)
        self.qmax = get_q(49.5, 49.5, detector.distance, source.wavelength)

        self.qstep = len(x_0)
        x = np.linspace(start=-1 * self.qmax,
                        stop=self.qmax,
                        num=self.qstep,
                        endpoint=True)
        y = np.linspace(start=-1 * self.qmax,
                        stop=self.qmax,
                        num=self.qstep,
                        endpoint=True)
        self.data.x_bins = x
        self.data.y_bins = y
        self.data = reader2D_converter(self.data)

    def test_ring_flat_distribution(self):
        """
            Test ring averaging
        """
        r = Ring(r_min=2 * self.qmin, r_max=5 * self.qmin,
                 center_x=self.data.detector[0].beam_center.x,
                 center_y=self.data.detector[0].beam_center.y)
        r.nbins_phi = 20

        o = r(self.data)
        for i in range(20):
            self.assertEqual(o.y[i], 1.0)

    def test_sectorphi_full(self):
        """
            Test sector averaging
        """
        r = SectorPhi(r_min=self.qmin, r_max=3 * self.qmin,
                      phi_min=0, phi_max=math.pi * 2.0)
        r.nbins_phi = 20
        o = r(self.data)
        for i in range(7):
            self.assertEqual(o.y[i], 1.0)

    def test_sectorphi_partial(self):
        """
        """
        phi_max = math.pi * 1.5
        r = SectorPhi(r_min=self.qmin, r_max=3 * self.qmin,
                      phi_min=0, phi_max=phi_max)
        self.assertEqual(r.phi_max, phi_max)
        r.nbins_phi = 20
        o = r(self.data)
        self.assertEqual(r.phi_max, phi_max)
        for i in range(17):
            self.assertEqual(o.y[i], 1.0)


class DataInfoTests(unittest.TestCase):

    def setUp(self):
        filepath = find('MAR07232_rest.h5')
        self.data_list = Loader().load(filepath)
        self.data = self.data_list[0]

    def test_ring(self):
        """
            Test ring averaging
        """
        r = Ring(r_min=.005, r_max=.01,
                 center_x=self.data.detector[0].beam_center.x,
                 center_y=self.data.detector[0].beam_center.y,
                 nbins=20)
        ##r.nbins_phi = 20

        o = r(self.data)
        filepath = find('ring_testdata.txt')
        answer_list = Loader().load(filepath)
        answer = answer_list[0]

        self.assertEqual(len(answer_list), 1)
        for i in range(r.nbins_phi - 1):
            self.assertAlmostEqual(o.x[i + 1], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i + 1], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i + 1], answer.dy[i], 4)

    def test_circularavg(self):
        """
        Test circular averaging
        The test data was not generated by IGOR.
        """
        r = CircularAverage(r_min=.00, r_max=.025,
                            bin_width=0.0003)
        r.nbins_phi = 20

        o = r(self.data)

        filepath = find('avg_testdata.txt')
        answer = Loader().load(filepath)[0]
        for i in range(r.nbins_phi):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)

    def test_box(self):
        """
            Test circular averaging
            The test data was not generated by IGOR.
        """

        r = Boxsum(x_min=.01, x_max=.015, y_min=0.01, y_max=0.015)
        s, ds, npoints = r(self.data)
        self.assertAlmostEqual(s, 34.278990899999997, 4)
        self.assertAlmostEqual(ds, 8.237259999538685, 4)
        self.assertAlmostEqual(npoints, 324.0000, 4)

        r = Boxavg(x_min=.01, x_max=.015, y_min=0.01, y_max=0.015)
        s, ds = r(self.data)
        self.assertAlmostEqual(s, 0.10579935462962962, 4)
        self.assertAlmostEqual(ds, 0.02542364197388483, 4)

    def test_slabX(self):
        """
            Test slab in X
            The test data was not generated by IGOR.
        """

        r = SlabX(x_min=-.01, x_max=.01, y_min=-0.0002,
                  y_max=0.0002, bin_width=0.0004)
        r.fold = False
        o = r(self.data)

        filepath = find('slabx_testdata.txt')
        answer = Loader().load(filepath)[0]
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)

    def test_slabY(self):
        """
            Test slab in Y
            The test data was not generated by IGOR.
        """

        r = SlabY(x_min=.005, x_max=.01, y_min=-
                  0.01, y_max=0.01, bin_width=0.0004)
        r.fold = False
        o = r(self.data)

        filepath = find('slaby_testdata.txt')
        answer = Loader().load(filepath)[0]
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)

    def test_sectorphi_full(self):
        """
            Test sector averaging I(phi)
            When considering the whole azimuthal range (2pi),
            the answer should be the same as ring averaging.
            The test data was not generated by IGOR.
        """

        nbins = 19
        phi_min = math.pi / (nbins + 1)
        phi_max = math.pi * 2 - phi_min

        r = SectorPhi(r_min=.005,
                      r_max=.01,
                      phi_min=phi_min,
                      phi_max=phi_max,
                      nbins=nbins)
        o = r(self.data)

        filepath = find('ring_testdata.txt')
        answer = Loader().load(filepath)[0]
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)

    def test_sectorphi_quarter(self):
        """
            Test sector averaging I(phi)
            The test data was not generated by IGOR.
        """

        r = SectorPhi(r_min=.005, r_max=.01, phi_min=0, phi_max=math.pi / 2.0)
        r.nbins_phi = 20
        o = r(self.data)

        filepath = find('sectorphi_testdata.txt')
        answer = Loader().load(filepath)[0]
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)

    def test_sectorq_full(self):
        """
            Test sector averaging I(q)
            The test data was not generated by IGOR.
        """

        r = SectorQ(r_min=.005, r_max=.01, phi_min=0, phi_max=math.pi / 2.0)
        r.nbins_phi = 20
        o = r(self.data)

        filepath = find('sectorq_testdata.txt')
        answer = Loader().load(filepath)[0]
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)

    def test_sectorq_log(self):
        """
            Test sector averaging I(q)
            The test data was not generated by IGOR.
        """

        r = SectorQ(r_min=.005, r_max=.01, phi_min=0, phi_max=math.pi / 2.0, base=10)
        r.nbins_phi = 20
        o = r(self.data)

        expected_binning = np.logspace(np.log10(0.005), np.log10(0.01), 20, base=10)
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], expected_binning[i], 3)

        # TODO: Test for Y values (o.y)
        # print len(self.data.x_bins)
        # print len(self.data.y_bins)
        # print self.data.q_data.shape
        # data_to_bin = np.array(self.data.q_data)
        # data_to_bin = data_to_bin.reshape(len(self.data.x_bins), len(self.data.y_bins))
        # H, xedges, yedges, binnumber = binned_statistic_2d(self.data.x_bins, self.data.y_bins, data_to_bin,
        #     bins=[[0, math.pi / 2.0], expected_binning], statistic='mean')
        # xedges_width = (xedges[1] - xedges[0])
        # xedges_center = xedges[1:] - xedges_width / 2

        # yedges_width = (yedges[1] - yedges[0])
        # yedges_center = yedges[1:] - yedges_width / 2

        # print H.flatten().shape
        # print o.y.shape


if __name__ == '__main__':
    unittest.main()
