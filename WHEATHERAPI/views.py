from rest_framework.response import Response
from rest_framework.views import APIView
import  requests

class WeatherByName(APIView):
    api_key="4a2b242084f2d9325a8d5b3dbd2de2a3"
    def get(self,*args,**kwargs):

        response=requests.get(
            url=f"https://api.openweathermap.org/data/2.5/weather?q={kwargs['city_name']}&appid={self.api_key}"
        )


        return Response(data={"data":response.json()})