from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
  def calculate(self,request:FlaskRequest) -> None: # type: ignore
    body = request.json
    input_data = self.__validate_body(body)
    calc_average = self.__calculate_average(input_data)
    response = self.__formated_response(calc_average)
    return response


  def __validate_body(self,body: Dict) -> List[float]:
    if "numbers" not in body:
      raise Exception("Body mal formatado!")
    input_data = body["numbers"]
    return input_data

  def __calculate_average(self,numbers: List[float]) -> Dict: # type: ignore
    if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
      raise HttpUnprocessableEntityError("Body mal formatado!")

    average = sum(numbers) / len(numbers)
    return average
  
  def __formated_response(self,average: float) -> Dict:
    return {
      "data":{
        "Calculator":4,
        "result": round(average, 2)
      }
    }