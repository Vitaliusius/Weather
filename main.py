import requests


LOCATION = ['cherepovets', 'london', 'svo']


def weather(location):
    url_template = 'https://wttr.in/{}'
    url = url_template.format(location)
    payload = {
        'T': '',
        'n': '',
        'M': '',
        'q': '',
        'lang': 'ru'
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response


def main():
    for town in LOCATION:
        response = weather(town)
        print(response.text)


if __name__ == '__main__':
    main()
