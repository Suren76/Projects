import pyowm
from accuweather import AccuWeather, ApiError, InvalidApiKeyError, InvalidCoordinatesError, RequestsExceededError
from aiohttp import ClientError, ClientSession
import asyncio
import logging

# OpenWeatherMap
key_1 = "3fd60d0b7b747ee2b82669d7cc84b4e0"
owm = pyowm.OWM(api_key=key_1)
w = owm.weather_manager().weather_at_id(614455).weather

print(w, '\n', w.temperature('celsius'), w.humidity)




# AccuWeather ######################################################################################
LOCATION_KEY = '11586'
API_KEY = "CFEvIq8sL9Lq6JoJSQvK0XPpjUeYoX66"
LATITUDE = 39.504664648
LONGITUDE = 46.336498654

# logging.basicConfig(level=logging.DEBUG)

async def main():
    async with ClientSession() as web_session:
        accuweather = AccuWeather(
            API_KEY, web_session, latitude=LATITUDE, longitude=LONGITUDE
        )
        current_conditions = await accuweather.async_get_current_conditions()
        forecast = await accuweather.async_get_forecast(metric=True)

        # print(f"Location: {accuweather.location_name} ({accuweather.location_key})")
        print(f"Requests remaining: {accuweather.requests_remaining}")
        print(f"Current: {current_conditions}")
        #[print(f) for f in forecast]


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# loop.close()


