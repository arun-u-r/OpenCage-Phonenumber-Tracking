import phonenumbers
from phonenumbers import geocoder
import folium
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENCAGE_SECRRET_KEY')
number = os.getenv('PHONE_NUMBER')

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(api_key)

query = str(number_location)
results = geocoder.geocode(query)

if not results:
    raise ValueError("Geocoding failed, no results returned")

lattitude = results[0]['geometry']['lat']
longitude= results[0]['geometry']['lng']
print(lattitude, longitude)

map_location = folium.Map(location = [lattitude, longitude], zoom_start = 9)
folium.Marker([lattitude, longitude], popup = number_location).add_to(map_location)
map_location.save("mylocation.html")