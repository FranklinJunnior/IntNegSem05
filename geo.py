from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

geolocator = Nominatim(user_agent="mi_aplicacion")

try:
    location = geolocator.geocode("Madrid, España")
    if location:
        print((location.latitude, location.longitude))
    else:
        print("No se pudo encontrar la ubicación.")
except GeocoderTimedOut:
    print("Error: La solicitud al servicio de geocodificación ha expirado.")
except GeocoderServiceError as e:
    print(f"Error del servicio de geocodificación: {e}")
