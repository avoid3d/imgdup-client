import requests


DEFAULT_BASE_URL = 'https://imgdup.herokuapp.com'


class ImgDupClient():
    def __init__(self, access_token, base_url=DEFAULT_BASE_URL):
        self.session = requests.Session()
        self.access_token = access_token
        self.base_url = base_url

    def process_image(self, image_file):
        path = '/images/actions/process-image'
        response = self.session.post(self.base_url + path, files={'image_uploadfile': image_file})
        response.raise_for_status()
        return response.json()
