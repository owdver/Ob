import requests

def spell_check(text):
    response = requests.post(
        'https://api.textrazor.com',
        data={'text': text},
        headers={'x-textrazor-key': 'YOUR_TEXTRAZOR_API_KEY'}
    )
    return response.json().get('response', {}).get('cleaned_text', text)

def shorten_url(long_url):
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        json={"long_url": long_url},
        headers={'Authorization': 'Bearer YOUR_BITLY_API_KEY'}
    )
    return response.json().get('link')