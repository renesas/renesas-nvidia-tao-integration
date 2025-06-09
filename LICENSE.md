# License Summary

## 1. Renesas Components

| Component                                 | Copyright                      | License        |
|-------------------------------------------|--------------------------------|----------------|
| Renesas AI Model Deployer                 | Renesas Electronics Corporation | BSD-3-Clause   |
| MCU application code                      | Renesas Electronics Corporation | BSD-3-Clause   |
| MPU application code                      | Renesas Electronics Corporation | Apache-2.0     |
| Modified NVIDIA TAO Tutorials (Jupyter)   | Renesas-NVIDIA Corporation      | Apache-2.0     |

---

## 2. Third-Party Dependencies

| Name                  | License                                                                 | Notes                                  |
|-----------------------|-------------------------------------------------------------------------|----------------------------------------|
| NVIDIA TAO Toolkit     | [TAO Toolkit SLA](https://developer.nvidia.com/tao-toolkit-license) | Not distributed; installed via script |
| NVIDIA CUDA Runtime    | [CUDA EULA](https://docs.nvidia.com/cuda/eula/index.html)       | Not distributed;installed via script  |
| tqdm                  | Mozilla Public License 2.0 (MPL 2.0)                                   | Installed via pip; used at runtime; not distributed or modified. |
| axe-core              | Mozilla Public License 2.0 (MPL 2.0)                                   |  Included in the Renesas AI Model Deployer GUI ; unmodified |
| certifi               | Mozilla Public License 2.0 (MPL 2.0)                                   |  Installed via pip; used at runtime; not distributed or modified.|
| fqdn                  | Mozilla Public License 2.0 (MPL 2.0)                                   | Installed via pip; used at runtime; not distributed or modified. |
| chardet               | GNU Lesser General Public License (LGPL)                               | Installed via pip; used at runtime; not distributed or modified. |

---

> **Notes**
>
>- **NVIDIA TAO Toolkit and CUDA Runtime are not distributed** in this release. They are installed via scripts that download them from NVIDIA servers. Users must review and agree to their respective license terms.
>- Full license texts for open-source components are included in the `/licenses_PYTHON_modules` directory inside the release package.
>- For third party OSS libraries in embedded code, please check the source code itself.

---

## BSD 3-Clause License

Copyright 2020 - 2025, Renesas Electronics Corporation and/or its affiliates

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




