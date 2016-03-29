"""
@brief      test log(time=10s)

"""
import os
import sys
import unittest


try:
    import src
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.special.propagation_epidemic import simulation


class TestEpidemicPropagation(unittest.TestCase):

    def test_simulation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = simulation(fLOG=fLOG, iter=100)
        fLOG(res)

if __name__ == "__main__":
    unittest.main()
