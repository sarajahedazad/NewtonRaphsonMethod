import newton_solver as ns 
import numpy as np
import pytest
import sympy

def test_newtonsolver():
    n = 1  # Number of variables
    x = sympy.symbols(f'x:{n}')

    F = sympy.Matrix([ x[0]**3- 4 *x[0] ])
    J = F.jacobian(x)
    x0 = np.array([ 6 ])

    found = ns.solver( F, J, x, x0, verbose = True)
    known = 2
    assert np.isclose( known , found )
