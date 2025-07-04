# Copyright 2018-2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""This module contains decompositions for (numerically-specified) arbitrary
unitary operations into sequences of elementary operations.
"""

from .unitary_decompositions import (
    one_qubit_decomposition,
    two_qubit_decomposition,
    multi_qubit_decomposition,
)
from .solovay_kitaev import sk_decomposition
from .ross_selinger import rs_decomposition
from .controlled_decompositions import ctrl_decomp_bisect, ctrl_decomp_zyz
