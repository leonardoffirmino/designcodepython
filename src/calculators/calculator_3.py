from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List

class Calculator3:
    def __init__(self,driver_handler: DriverHandlerInterface) -> None:
      self.__driver_handler = driver_handler

  
    def calculate(self, request:FlaskRequest) -> Dict: # type: ignore
      body = request.json
      input_data = self.__validate_body(body)



    def __validate_body(self,body: Dict) -> List[float]:
      if "numbers" not in body:
        raise Exception("body mal formatado!")
      
      input_data = body["numbers"]
      return input_data

    def __calculate_multiplication(self, numbers: List[float]) -> None:
       multiplication = 1
       for num in numbers:
           multiplication *= num

       return multiplication
   
   