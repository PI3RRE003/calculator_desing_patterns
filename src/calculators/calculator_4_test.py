from .calculator_4 import Calculator4
from typing import Dict, List
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def average(self, numbers:List[float]) -> float:
        return 3
    
class MockDriverHandlerError:
    def variance(self, numbers:List[float]) -> float:
        return 0
    
def test_calculate_with_average_error():
    mock_request = MockRequest({ "numbers" : [0, 0, 0,]})
    calculator_4 = Calculator4(MockDriverHandlerError())
    
    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)
   
    assert str(excinfo.value) == 'Falha no processo: Média 0'


def test_calculate():
    mock_request = MockRequest({ "numbers" : [1,2,3]})
    calculator_4 = Calculator4(MockDriverHandler())
    
    response = calculator_4.calculate(mock_request)
    assert response == {'data': {'Calculator': 4, 'value': 3, 'Success': True}}
    print()
    print(response)
   