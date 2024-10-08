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

obj = APIBase("torch.nn.functional.batch_norm")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
                                [-1.2533, -0.9829, -1.0981],
                                [ 0.1507, -1.1431, -2.0361]],

                                [[ 0.1024, -0.4482,  0.4137],
                                [ 0.9385,  0.4565,  0.7702],
                                [ 0.4135, -0.2587,  0.0482]]])
        data = torch.tensor([1., 1., 1.])
        result = F.batch_norm(input, data, data, data, data)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
                                [-1.2533, -0.9829, -1.0981],
                                [ 0.1507, -1.1431, -2.0361]],

                                [[ 0.1024, -0.4482,  0.4137],
                                [ 0.9385,  0.4565,  0.7702],
                                [ 0.4135, -0.2587,  0.0482]]])
        data = torch.tensor([1., 1., 1.])
        result = F.batch_norm(input=input, running_mean=data, running_var=data, weight=data, bias=data)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
         [-1.2533, -0.9829, -1.0981],
         [ 0.1507, -1.1431, -2.0361]],

        [[ 0.1024, -0.4482,  0.4137],
         [ 0.9385,  0.4565,  0.7702],
         [ 0.4135, -0.2587,  0.0482]]])
        running_mean = torch.tensor([1., 1., 1.])
        running_var = torch.tensor([1., 1., 1.])
        weight = torch.tensor([1., 1., 1.])
        bias = torch.tensor([1., 1., 1.])
        result = F.batch_norm(input=input, running_mean=running_mean, running_var=running_var, weight=weight, bias=bias, training=True, momentum=0.5)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
                                [-1.2533, -0.9829, -1.0981],
                                [ 0.1507, -1.1431, -2.0361]],

                                [[ 0.1024, -0.4482,  0.4137],
                                [ 0.9385,  0.4565,  0.7702],
                                [ 0.4135, -0.2587,  0.0482]]])
        data = torch.tensor([1., 1., 1.])
        result = F.batch_norm(input=input, running_mean=data, running_var=data, weight=data, bias=data, eps=1e-4)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
                                [-1.2533, -0.9829, -1.0981],
                                [ 0.1507, -1.1431, -2.0361]],

                                [[ 0.1024, -0.4482,  0.4137],
                                [ 0.9385,  0.4565,  0.7702],
                                [ 0.4135, -0.2587,  0.0482]]])
        data = torch.tensor([1., 1., 1.])
        result = F.batch_norm(input, data, data, data, data, False, 0.2, 1e-4)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)


# generated by validate_unittest autofix, based on test_case_5
def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
                                [-1.2533, -0.9829, -1.0981],
                                [ 0.1507, -1.1431, -2.0361]],

                                [[ 0.1024, -0.4482,  0.4137],
                                [ 0.9385,  0.4565,  0.7702],
                                [ 0.4135, -0.2587,  0.0482]]])
        data = torch.tensor([1., 1., 1.])
        result = F.batch_norm(input=input, running_mean=data, running_var=data, weight=data, bias=data, training=False, momentum=0.2, eps=1e-4)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)


# generated by validate_unittest autofix, based on test_case_5
def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
                                [-1.2533, -0.9829, -1.0981],
                                [ 0.1507, -1.1431, -2.0361]],

                                [[ 0.1024, -0.4482,  0.4137],
                                [ 0.9385,  0.4565,  0.7702],
                                [ 0.4135, -0.2587,  0.0482]]])
        data = torch.tensor([1., 1., 1.])
        result = F.batch_norm(eps=1e-4, momentum=0.2, training=False, bias=data, weight=data, running_var=data, running_mean=data, input=input)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)


# generated by validate_unittest autofix, based on test_case_5
def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
                                [-1.2533, -0.9829, -1.0981],
                                [ 0.1507, -1.1431, -2.0361]],

                                [[ 0.1024, -0.4482,  0.4137],
                                [ 0.9385,  0.4565,  0.7702],
                                [ 0.4135, -0.2587,  0.0482]]])
        data = torch.tensor([1., 1., 1.])
        result = F.batch_norm(input, data, data)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch.nn.functional as F
        import torch
        input = torch.tensor([[[ 1.1524,  0.4714,  0.2857],
         [-1.2533, -0.9829, -1.0981],
         [ 0.1507, -1.1431, -2.0361]],

        [[ 0.1024, -0.4482,  0.4137],
         [ 0.9385,  0.4565,  0.7702],
         [ 0.4135, -0.2587,  0.0482]]])
        running_mean = torch.tensor([1., 1., 1.])
        running_var = torch.tensor([0.5, 0.5, 0.5])
        weight = torch.tensor([1.5, 1.5, 1.5])
        bias = torch.tensor([0.5, 0.5, 0.5])
        result = F.batch_norm(input, running_mean, running_var, weight, bias, True, 0.5, 1e-4)
        """
    )
    obj.run(pytorch_code, ["result"], atol=1e-4)
