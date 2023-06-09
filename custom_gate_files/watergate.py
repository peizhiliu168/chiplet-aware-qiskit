# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Water gate."""
from math import pi

from typing import Optional
import numpy
from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import QuantumRegister


class WaterGate(Gate):
    r"""Water Gate
    Water gate is all "water"

    **Matrix Representation:**

    .. math::

        I = \begin{pmatrix}
                1 & 0 \\
                0 & 1
            \end{pmatrix}

    **Circuit symbol:**

    .. parsed-literal::
             ┌───┐
        q_0: ┤ W ├
             └───┘
    """

    def __init__(self, label: Optional[str] = None):
        """Create new Identity gate."""
        super().__init__("water", 1, [], label="Water")

    # def _define(self):
    #     """
    #     gate h a { u2(0,pi) a; }
    #     """
    #     # pylint: disable=cyclic-import
    #     from qiskit.circuit.quantumcircuit import QuantumCircuit
    #     from .u2 import U2Gate

    #     q = QuantumRegister(1, "q")
    #     qc = QuantumCircuit(q, name=self.name)
    #     rules = [(U2Gate(0, pi/69), [q[0]], [])]
    #     for instr, qargs, cargs in rules:
    #         qc._append(instr, qargs, cargs)

        # self.definition = qc

    def inverse(self):
        """Invert this gate."""
        return WaterGate()  # self-inverse

    def __array__(self, dtype=None):
        """Return a numpy.array for the identity gate."""
        return numpy.array([[1, 0], [0, 1]], dtype=dtype)

    def power(self, exponent: float):
        """Raise gate to a power."""
        return WaterGate()
