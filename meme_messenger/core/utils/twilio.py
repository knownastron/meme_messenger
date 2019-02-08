from twilio.rest import Client


class twilioObject(object):
    from_num = "+17175029477"
    account_sid = "AC5e1e2fda4c0bd09e860d3aeaefe2d43d"
    auth_token = "7c6a643301562fa877d1cf197f8e2956" #remember to decode


    def send_meme(self, to_num, url):
        plus_prepended_to_num = "+" + str(to_num)
        print("sending meme")
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            to= plus_prepended_to_num ,
            from_="+17175029477",
            body="Regards from Meme Messenger!",
            media_url = url
        )
        print(message.sid)

    def send_meme_fixed(self):

        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            to= "+13064910574",
            from_="+17175029477",
            # body="Hello from Jason's Python Twilio Script!"
            media_url = 'https://i.imgur.com/ZbesEFk.png'
        )
        print(message.sid)

    def send_confirmation(self, to_num):
        plus_prepended_to_num = "+" + str(to_num)
        print("sending confirmation")
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            to= plus_prepended_to_num,
            from_="+17175029477",
            body="You are registered to Meme Messenger! You will receive memes everyday at noon (MST)!"

        )
        print(message.sid)
