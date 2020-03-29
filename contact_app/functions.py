import requests
from flask import current_app

extra_fields = ['organization', 'title', 'website', 'location']


def enrich_details(**payload):
    api_url = 'https://api.fullcontact.com/v3/person.enrich'
    headers = {'Authorization': 'Bearer {token}'.format(token=current_app.config['FULLCONTACT_API_KEY'])}
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        json_response = response.json()
        return {field: json_response[field] for field in extra_fields if json_response.get(field)}
    else:
        return {}
