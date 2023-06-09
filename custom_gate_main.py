import numpy as np

from qiskit import QuantumCircuit, transpile
from qiskit.circuit import Parameter, Measure
from qiskit.transpiler import Target, InstructionProperties
from qiskit.circuit.library import UGate, RZGate, RXGate, RYGate, CXGate, CZGate, SwapGate, WaterGate, IGate


from fake_chiplet import FakeChiplet

backend = FakeChiplet()

qc1 = QuantumCircuit(12)

qc1.watergate(8)
qc1.h(0)
qc1.h(8)
qc1.swap(8,11)
qc1.swap(7,10)
qc1.h(8)
qc1.h(7)

print("iGate def: ", IGate().definition)
print(backend.instructions)

# target = backend.target.from_configuration(custom_name_mapping={"water":WaterGate()})
# backend._target = target

qc_basis = transpile(qc1, backend=backend,
                     optimization_level=0)
img = qc_basis.draw(output='mpl')

img.savefig("circuit2.png")
