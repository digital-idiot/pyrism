from __future__ import division

import numpy as np
from scipy.integrate import quad


class Orientation(object):
    def __init__(self):
        pass

    @staticmethod
    def gaussian(std=10.0, mean=0.0):
        """Gaussian probability distribution function (PDF) for orientation averaging.

        Parameters
        ----------
        std: int or float
            The standard deviation in degrees of the Gaussian PDF
        mean: int or float
            The mean in degrees of the Gaussian PDF.  This should be a number in the interval [0, 180)

        Returns
        -------
        pdf(x): callable
            A function that returns the value of the spherical Jacobian-normalized Gaussian PDF with the given STD at x
            (degrees). It is normalized for the interval [0, 180].
        """
        norm_const = 1.0

        def pdf(x):
            return norm_const * np.exp(-0.5 * ((x - mean) / std) ** 2) * \
                   np.sin(np.pi / 180.0 * x)

        norm_dev = quad(pdf, 0.0, 180.0)[0]
        # ensure that the integral over the distribution equals 1
        norm_const /= norm_dev
        return pdf

    @staticmethod
    def uniform():
        """Uniform probability distribution function (PDF) for orientation averaging.

        Returns
        -------
        pdf(x): callable
            A function that returns the value of the spherical Jacobian-normalized uniform PDF. It is normalized for
            the interval [0, 180].
        """
        norm_const = 1.0

        def pdf(x):
            return norm_const * np.sin(np.pi / 180.0 * x)

        norm_dev = quad(pdf, 0.0, 180.0)[0]
        # ensure that the integral over the distribution equals 1
        norm_const /= norm_dev
        return pdf
