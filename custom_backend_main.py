import numpy as np

from qiskit import QuantumCircuit, transpile
from qiskit.circuit import Parameter, Measure
from qiskit.transpiler import Target, InstructionProperties
from qiskit.circuit.library import UGate, RZGate, RXGate, RYGate, CXGate, CZGate, SwapGate


from fake_chiplet import FakeChiplet

backend = FakeChiplet()

# Generate example circuit
qc = QuantumCircuit(12, 12)

qc.h(0)
qc.x(1)
qc.h(0)
qc.h(6)

qc.h(8)
qc.swap(8,11)
qc.swap(7,10)
qc.h(8)
qc.h(7)


qc_basis = transpile(qc, backend=backend, optimization_level=3)
img = qc_basis.draw(output='mpl')
img.savefig("circuit1.png")

qc_basis = transpile(qc_basis, 
                     backend=backend, 
                     optimization_level=3, 
                     initial_layout=[0,1,2,3,4,5,6,8,7,9, 11, 10])
# [0,6,2,10,8,7,1,5,4,11,3,9]
img = qc_basis.draw(output='mpl')
img.savefig("circuit2.png")
