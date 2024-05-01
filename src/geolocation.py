try:
    from geopy.geocoders import Nominatim
    from src.api_cep import ConsultZip
    import time
except Exception as e:
    print(f"Lib not installed: %s" % e)

class Geocoder:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="geoapiExercises")
        self.consult = ConsultZip()
        self.attempts = 0

    @staticmethod
    def zip_adjust(cep):
        cep_str = str(cep)
        if len(cep_str) < 8:
            cep_str = '0' + cep_str
        return cep_str

    def geocode(self, zip):
        try:
            location = self.geolocator.geocode(zip)
            city, street = self.consult.search_zip(zip=str(zip))
            location_street = self.geolocator.geocode(f"{street}, {city}")
            location_city = self.geolocator.geocode(city)
            if location:
                return location.latitude, location.longitude
            if location_street:
                return location_street.latitude, location_street.longitude
            if location_city:
                return location_city.latitude, location_city.longitude
            else:
                return None
        except Exception as e:
            self.attempts += 1
            print(f"Attempts {self.attempts} - Error geocoding zip code {zip}: {str(e)}")
            if self.attempts >= 5:
                self.attempts = 0
                return None
            time.sleep(60)
            return self.geocode(zip)
