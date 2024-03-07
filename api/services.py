import requests
from datetime import datetime
from django.core.cache import cache
from typing import Dict, Union




def get_age_from_agify(name: str) -> Union[int, None]:
    response = requests.get(f"https://api.agify.io/?name={name}")
    if response.status_code == 200:
        data = response.json()
        return data.get('age')
    else:
        return None

def get_age_and_dob(name: str) -> Dict[str, Union[str, int]]:
    cached_response = cache.get(name)
    if cached_response:
        return cached_response
    else:
        age = get_age_from_agify(name)
        if age is None:
            raise Exception('Failed to fetch age from Agify API')
        else:
            current_year = datetime.now().year
            dob_year = current_year - age
            dob = datetime(dob_year, 1, 1).date()
            response_data = {'name': name, 'age': age, 'date_of_birth': dob.strftime('%Y')}
            cache.set(name, response_data, timeout=3600 * 24)
            return response_data
