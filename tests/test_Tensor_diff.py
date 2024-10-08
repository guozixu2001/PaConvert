# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.Tensor.diff")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2])
        result = x.diff()
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2])
        b = torch.tensor([4, 5])
        result = x.diff(append=b)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, 2, 3], [3, 4, 5]])
        result = x.diff(dim=1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, 2, 3], [3, 4, 5]])
        result = x.diff(2, dim=1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2])
        b = torch.tensor([4, 5])
        result = x.diff(n=1, prepend=b)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2])
        b = torch.tensor([4, 5])
        c = torch.tensor([4, 5])
        result = x.diff(n=1, dim=-1, prepend=b, append=c)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2])
        b = torch.tensor([4, 5])
        c = torch.tensor([4, 5])
        result = x.diff(1, -1, b, c)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2])
        b = torch.tensor([4, 5])
        c = torch.tensor([4, 5])
        result = x.diff(append=c, n=1, dim=-1, prepend=b)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2, 10])
        b = torch.tensor([4, 5])
        result = x.diff(n=2, prepend=b)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_10():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2, 10])
        b = torch.tensor([4, 5])
        result = x.diff(n=3, append=b, prepend=b)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_11():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1, 3, 2, 10])
        b = torch.tensor([4, 5])
        result = x.diff(n=4, append=b)
        """
    )
    obj.run(pytorch_code, ["result"])
