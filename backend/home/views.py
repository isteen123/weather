from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class WeatherAPIView(APIView):
    def get(self, request):
        location = request.query_params.get('location')
        if not location:
            return Response({'error': 'Location parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        api_key = '546ff1dbc9e07f70cc45204faf814544'
        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        
        try:
            response = requests.get(api_url)
            data = response.json()
            
            weather_data = {
                'location': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'conditions': data['weather'][0]['description'],
            }
            
            return Response(weather_data)
        except Exception as e:
            return Response({'error': 'Unable to fetch weather data.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
