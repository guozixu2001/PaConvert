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

obj = APIBase("torchvision.models.wide_resnet50_2")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torchvision
        wide_resnet50_2 = torchvision.models.wide_resnet50_2()
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        wide_resnet50_2 = paddle.vision.models.wide_resnet50_2(pretrained=False)
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
        wide_resnet50_2 = torchvision.models.wide_resnet50_2(weights=None, progress=False)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        wide_resnet50_2 = paddle.vision.models.wide_resnet50_2(progress=False,
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
        wide_resnet50_2 = torchvision.models.wide_resnet50_2(progress=True, weights='DEFAULT')
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        wide_resnet50_2 = paddle.vision.models.wide_resnet50_2(progress=True,
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
        wide_resnet50_2 = torchvision.models.wide_resnet50_2(weights=torchvision.models.Wide_ResNet50_2_Weights.DEFAULT)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        wide_resnet50_2 = paddle.vision.models.wide_resnet50_2(pretrained=True)
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
        wide_resnet50_2 = torchvision.models.wide_resnet50_2(progress=True)
        """
    )
    paddle_code = textwrap.dedent(
        """
        import paddle
        wide_resnet50_2 = paddle.vision.models.wide_resnet50_2(progress=True,
            pretrained=False)
        """
    )
    obj.run(
        pytorch_code,
        expect_paddle_code=paddle_code,
    )