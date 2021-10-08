from pprint import pprint
import sys
import os

from imgdup import ImgDupClient
import imgdup


def main():
    client = ImgDupClient(
        base_url=os.environ.get('IMGDUP_BASE_URL'),
        access_token=os.environ['IMGDUP_ACCESS_TOKEN']
    )

    with open(sys.argv[1], 'rb') as image_file:
        process_image_response = client.process_image(image_file)
    
    pprint('process image response:')
    pprint(process_image_response)


if __name__ == '__main__':
    main()