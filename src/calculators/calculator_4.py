from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpunprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator4:
    def __init__(self, driver_handle: DriverHandlerInterface) -> None:
        self.__driver_handle = driver_handle

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        average = self.__calculate_average(input_data)
        self.__verify_results(average)

        formated_response = self.__format_response(average)
        return formated_response
    
    def __calculate_average(self, numbers: List[float]) -> float:
        average = self.__driver_handle.average(numbers)
        return average
    
    def __verify_results(self, average:float) -> None:
        if average < 0:
            raise HttpBadRequestError('Falha no processo: Média 0')

    
    def __validate_body(self, body:Dict) -> List[float]:            
        if "numbers" not in body:
            raise HttpunprocessableEntityError('body mal formatado')
        
        input_data = body["numbers"]
        return input_data
    
    def __format_response(self, average:float) -> Dict:
        return {
            "data" : {
                "Calculator" : 4,
                "value" : average,
                "Success" : True
            }
        }