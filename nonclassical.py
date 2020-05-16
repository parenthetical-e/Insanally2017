"""A sketch of reimplementation of Insanally 2017."""
import numpy as np
import sklearn as sk
import statsmodels as sm


def create_isis(times):
    """Calc ISIs for a 1darray of spikes times"""
    if times.ndim > 1:
        raise ValueError("times must be 1d")

    return np.diff(times)


# KDE based estimator
# Fit BW by CV? Or have seperate class? Prob. the latter. Use sklearn.
# KDE - this is a thin wrapper, or use the raw import and not have this
# at all?
class Dist():
    def __init__(self, bw):
        pass

    def train(self, isis):
        pass

    def probs(self, isi):
        pass

    def reset_probs(self, p=0.5):
        pass


# TimeSeriesKDE - builds in Dist. Buildings rolling window
# of dists for p(sis).
class TemporalDist():
    def __init__(self, bw, window, shift):
        pass

    def train(self, isis):
        pass

    def probs(self, isi):
        pass


# Behave prob - est from the actual trials
# which we assume is series of ints
class Behave():
    def __init__(self, conds):
        pass

    def train(self, trials):
        pass

    def probs(self, cond):
        pass

    def probs_other(self, cond):
        # returns all the prob of all other conds, not cond
        # It is a simple convenience func
        return None


# Cond agnostic bayes decoder.
#
# Needs to rerun for each cond in Behave.
#
# It assumes we have pre-trained Dist, TemporalDist, Behave meaning
# a seperate train() loop is needed, but it is not defined here.
def decode(isis, cond, dist, behave, p0=0.5):
    probs = np.zeros(isis.shape[0] + 1)
    probs[0] = p0

    for i in range(isis.shape[0]):
        p_i = None  # bayes goes here
        probs[i + 1] = p_i

    return probs  # 1d array
