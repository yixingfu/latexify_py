# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math
import pytest

from latexify import with_latex


def solve(a, b, c):
  return (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

solve_latex = r'\mathrm{solve}(a, b, c) \triangleq \frac{-b + \sqrt{b^{2} - 4ac}}{2a}'

def solve_with_assign(a, b, c):
  numerator = (-b + math.sqrt(b ** 2 - 4 * a * c))
  denominator = 2 * a
  return numerator / denominator

solve_with_assign_latex = r'\mathrm{solve_with_assign}(a, b, c) \triangleq \frac{-b + \sqrt{b^{2} - 4ac}}{2a}'


def sinc(x):
  if x == 0:
    return 1
  else:
    return math.sin(x) / x


sinc_latex = (
  r'\mathrm{sinc}(x) \triangleq \left\{ \begin{array}{ll} 1, & \mathrm{if} \ x=0 \\ '
  r'\frac{\sin{\left({x}\right)}}{x}, & \mathrm{otherwise} \end{array} \right.'
)


def xtimesbeta(x, beta):
  return x * beta


xtimesbeta_latex = r'\mathrm{xtimesbeta}(x, {\beta}) \triangleq x{\beta}'
xtimesbeta_latex_no_symbols = r'\mathrm{xtimesbeta}(x, beta) \triangleq xbeta'


func_and_latex_str_list = [
  (solve, solve_latex, None),
  (solve_with_assign, solve_with_assign_latex, None),
  (sinc, sinc_latex, None),
  (xtimesbeta, xtimesbeta_latex, True),
  (xtimesbeta, xtimesbeta_latex_no_symbols, False),
]


@pytest.mark.parametrize(
  'func, expected_latex, math_symbol',
  func_and_latex_str_list
)
def test_with_latex_to_str(func, expected_latex, math_symbol):
  if math_symbol is None:
    latexified_function = with_latex(func)
  else:
    latexified_function = with_latex(math_symbol=math_symbol)(func)
  print(str(latexified_function))
  assert str(latexified_function) == expected_latex
  assert expected_latex in latexified_function._repr_latex_()
