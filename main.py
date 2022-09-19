import requests, json

VK_USER_ID = 'ID'
VK_TOKEN = 'TOKEN'


def get_photo_data(offset = 0, count = 10):
    api_vk = requests.get('https://api.vk.com/method/photos.getALL', params={
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'offset': 0,
        'count': count,
        'photo_sizes': 0,
        'v': 5.103
    })
    return json.loads(api_vk.text)

def main():
    print(get_photo_data())

if __name__ == "__main__":
    main()