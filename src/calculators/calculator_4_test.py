from .calculator_4 import Calculator4 
from pytest import raises
from typing import Dict


class MockRequest:
  def __init__(self,body:Dict)-> None:
    self.json = body
  

  def test_calculate():
    mock_request = MockRequest({"numbers": [20,30,40,50]})
    calculator_4 = Calculator4(MockRequest())

    reponse = calculator_4.calculate(mock_request)

    assert reponse == {'data': {'Calculator': 3,
        'value': 1000000,
        'Success': True,
        }
    }

def test_calculate_with_body_error():
  mock_request = MockRequest(body={"something": 1})
  
  calculator_4 = Calculator4()

  with raises(Exception) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value)== "Body mal formatado!"
