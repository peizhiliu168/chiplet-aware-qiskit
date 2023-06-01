import numpy as np

from qiskit import QuantumCircuit, transpile
from qiskit.circuit import Parameter, Measure
from qiskit.transpiler import Target, InstructionProperties
from qiskit.circuit.library import UGate, RZGate, RXGate, RYGate, CXGate, CZGate, SwapGate
from qiskit.circuit.library.standard_gates.watergate1 import WaterGate1

target = Target(num_qubits=12)
target.add_instruction(CXGate(), {(0, 1): InstructionProperties(error=.0001, duration=5e-7)})
target.add_instruction(
    UGate(Parameter('theta'), Parameter('phi'), Parameter('lam')),
    {
        (0,): InstructionProperties(error=.00001, duration=5e-8),
        (1,): InstructionProperties(error=.00001, duration=5e-8),
        (2,): InstructionProperties(error=.00001, duration=5e-8),
        (3,): InstructionProperties(error=.00001, duration=5e-8),
        (4,): InstructionProperties(error=.00001, duration=5e-8),
        (5,): InstructionProperties(error=.00001, duration=5e-8),
        (6,): InstructionProperties(error=.00001, duration=5e-8),
        (7,): InstructionProperties(error=.00001, duration=5e-8), 
        (8,): InstructionProperties(error=.00001, duration=5e-8)
    }
)
target.add_instruction(
    RZGate(Parameter('theta')),
    {
        (0,): InstructionProperties(error=.00001, duration=5e-8),
        (1,): InstructionProperties(error=.00001, duration=5e-8),
        (2,): InstructionProperties(error=.00001, duration=5e-8),
        (3,): InstructionProperties(error=.00001, duration=5e-8),
        (4,): InstructionProperties(error=.00001, duration=5e-8),
        (5,): InstructionProperties(error=.00001, duration=5e-8),
        (6,): InstructionProperties(error=.00001, duration=5e-8),
        (7,): InstructionProperties(error=.00001, duration=5e-8), 
        (8,): InstructionProperties(error=.00001, duration=5e-8)
    }
)
target.add_instruction(
    RYGate(Parameter('theta')),
    {
        (0,): InstructionProperties(error=.00001, duration=5e-8),
        (1,): InstructionProperties(error=.00001, duration=5e-8),
        (2,): InstructionProperties(error=.00001, duration=5e-8),
        (3,): InstructionProperties(error=.00001, duration=5e-8),
        (4,): InstructionProperties(error=.00001, duration=5e-8),
        (5,): InstructionProperties(error=.00001, duration=5e-8),
        (6,): InstructionProperties(error=.00001, duration=5e-8),
        (7,): InstructionProperties(error=.00001, duration=5e-8), 
        (8,): InstructionProperties(error=.00001, duration=5e-8)
    }
)
target.add_instruction(
    RXGate(Parameter('theta')),
    {
        (0,): InstructionProperties(error=.00001, duration=5e-8),
        (1,): InstructionProperties(error=.00001, duration=5e-8),
        (2,): InstructionProperties(error=.00001, duration=5e-8),
        (3,): InstructionProperties(error=.00001, duration=5e-8),
        (4,): InstructionProperties(error=.00001, duration=5e-8),
        (5,): InstructionProperties(error=.00001, duration=5e-8),
        (6,): InstructionProperties(error=.00001, duration=5e-8),
        (7,): InstructionProperties(error=.00001, duration=5e-8), 
        (8,): InstructionProperties(error=.00001, duration=5e-8)
    }
)
target.add_instruction(
    CZGate(),
    {
        (0, 3): InstructionProperties(error=.0001, duration=5e-7),
        (1, 4): InstructionProperties(error=.0001, duration=5e-7),
        (2, 5): InstructionProperties(error=.0001, duration=5e-7),
        (3, 4): InstructionProperties(error=.0001, duration=5e-7),
        (4, 5): InstructionProperties(error=.0001, duration=5e-7),
        (3, 6): InstructionProperties(error=.0001, duration=5e-7),
        (4, 7): InstructionProperties(error=.0001, duration=5e-7),
        (5, 8): InstructionProperties(error=.0001, duration=5e-7),
    }
)
target.add_instruction(
    Measure(),
    {
        (0,): InstructionProperties(error=.00001, duration=5e-8),
        (1,): InstructionProperties(error=.00001, duration=5e-8),
        (2,): InstructionProperties(error=.00001, duration=5e-8),
        (3,): InstructionProperties(error=.00001, duration=5e-8),
        (4,): InstructionProperties(error=.00001, duration=5e-8),
        (5,): InstructionProperties(error=.00001, duration=5e-8),
        (6,): InstructionProperties(error=.00001, duration=5e-8),
        (7,): InstructionProperties(error=.00001, duration=5e-8), 
        (8,): InstructionProperties(error=.00001, duration=5e-8)
    }
)
target.add_instruction(
    SwapGate(),
    {
        (0, 3): InstructionProperties(error=.0001, duration=5e-7),
        (3, 6): InstructionProperties(error=.0001, duration=5e-7),
        (1, 4): InstructionProperties(error=.0001, duration=5e-7),
        (4, 7): InstructionProperties(error=.0001, duration=5e-7),
        (2, 5): InstructionProperties(error=.0001, duration=5e-7),
        (5, 8): InstructionProperties(error=.0001, duration=5e-7),
        (3, 4): InstructionProperties(error=.0001, duration=5e-7),
        (4, 5): InstructionProperties(error=.0001, duration=5e-7),
        (6, 9): InstructionProperties(error=.01, duration=1e-6),
        (7, 10): InstructionProperties(error=.01, duration=1),
        (8, 11): InstructionProperties(error=.01, duration=1), 
    }
)

img = target.build_coupling_map().draw()
img.save("coupling_map.png")


# Generate example circuit
qc = QuantumCircuit(12, 12)

qc.h(0)
qc.x(1)
qc.h(0)
qc.h(6)

qc.swap(8,10)
qc.swap(7,11)
qc.h(8)
qc.h(7)

from fake_chiplet import FakeChiplet

backend = FakeChiplet()

qc_basis = transpile(qc, backend=backend, optimization_level=3)
img = qc_basis.draw(output='mpl')
img.savefig("circuit1.png")

# qc1 = QuantumCircuit(12)
# qc1.i(0)
# qc1.i(1)
# custom = qc1.to_gate().control(2)


# qc1.watergate1(9,6)
# qc1.watergate1(1,2)

# target = backend.target.from_configuration(custom_name_mapping={"watergate1":WaterGate1()})
# backend._target = target

# qc_basis = transpile(qc1, backend=backend,#range(9)) + [9,10,11],
#                      optimization_level=3)
# img = qc_basis.draw(output='mpl')

# img.savefig("circuit2.png")

# from qiskit.visualization import plot_circuit_layout

# img = plot_circuit_layout(qc_basis)
# img.savefig("layout.png")