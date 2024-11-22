# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
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
#
import textwrap

from apibase import APIBase

obj = APIBase("torchvision.models.resnext101_64x4d")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        resnext101_64x4d = torchvision.models.resnext101_64x4d()
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        resnext101_64x4d = paddle.vision.models.resnext101_64x4d(pretrained=False)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        resnext101_64x4d = torchvision.models.resnext101_64x4d(weights=None, progress=False)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        resnext101_64x4d = paddle.vision.models.resnext101_64x4d(progress=False,
            pretrained=False)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        resnext101_64x4d = torchvision.models.resnext101_64x4d(progress=True, weights='DEFAULT')
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        resnext101_64x4d = paddle.vision.models.resnext101_64x4d(progress=True,
            pretrained=True)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        resnext101_64x4d = torchvision.models.resnext101_64x4d(weights=torchvision.models.ResNet101_64x4d_Weights.DEFAULT)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        resnext101_64x4d = paddle.vision.models.resnext101_64x4d(pretrained=True)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        resnext101_64x4d = torchvision.models.resnext101_64x4d(progress=True)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        resnext101_64x4d = paddle.vision.models.resnext101_64x4d(progress=True,
            pretrained=False)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )