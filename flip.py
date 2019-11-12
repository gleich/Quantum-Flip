from projectq.ops import H, Measure
from projectq import MainEngine

def get_qubit(quantum_engine):
    """Gets the current status of the qubit

    Arguments:
        quantum_engine {projectq.cengines._main.MainEngine} -- The quantum computer simulation engine

    Returns:
        [int] -- [status of the qubit]
    """
    qubit = quantum_engine.allocate_qubit()
    H | qubit
    Measure | qubit
    qubit_status = int(qubit)
    return qubit_status

engine = MainEngine
print(get_qubit(engine))
quantum_engine.flush()
