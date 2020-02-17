import numpy as np
import numpy.testing as npt

import InsightDC2

def test_InsightDC2_smoke():
    #Smoke test
    obj = InsightDC2.DC2object()

def test_InsightDC2_fizz():
    #Test the fizz function
    obj = InsightDC2.DC2object()
    output = obj.fizz()
    
    npt.assert_equal(output, "buzz")
