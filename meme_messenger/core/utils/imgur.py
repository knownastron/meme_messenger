from imgurpython import ImgurClient

class imgurObject(object):
    client_id = 'dcde5085d567db7'
    client_secret = 'bdbf1067a0917dd85d4fe0f15b62d06615e184e7' #remembe to decode
    album_id = 'xxns9DM'

    def __init__(self):
        pass

    def getURLs(self):
        client = ImgurClient(self.client_id, self.client_secret)

        img_links = client.get_album_images(self.album_id)
        return img_links
