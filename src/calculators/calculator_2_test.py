from typing import Dict
from .calculator_2 import Calculator2

class MockRequest:
  def __init__(self,body: Dict)-> None:
    self.json = body


def test_calculate():
  mock_request = MockRequest({ "numbers": [2.33,2.11,5.44]})
  
  calculator2 = Calculator2()
  formated_reponse = calculator2.calculate(mock_request)
  print()
  print(formated_reponse)

  assert isinstance(formated_reponse,dict)
  assert formated_reponse == {'data': {'Calculator': 2, 'result': 0.08}}