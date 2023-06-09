
"""
Fake chiplet device (12 qubit).
"""

import os
from qiskit.providers.fake_provider import fake_qasm_backend, fake_backend


class FakeChiplet(fake_backend.FakeBackendV2):
    """A fake 5 qubit backend.

    .. code-block:: text

        0 ↔ 3 ↔ 6 -- 9
            ↕   
        1 ↔ 4 ↔ 7 -- 10
            ↕
        2 ↔ 5 ↔ 8 -- 11
    """
    
    dirname = os.path.dirname(__file__)
    print(dirname)
    conf_filename = "custom_backend/conf_chiplet.json"
    props_filename = "custom_backend/props_chiplet.json"
    backend_name = "fake_chiplet"
