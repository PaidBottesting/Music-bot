import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "d2d5ccf4592270fd54ad9e2014c960e7")
    BOT_TOKEN = os.environ.get("7759467837:AAGzJlrzCNJJ0-xnKkE9VGBgwc3qwkCr5qA",)
    STRING_SESSION = os.environ.get("STRING_SESSION", " BQBiMZkAUoGnnYY0CGEesTfwlWxZH8zSGOtrWqVfWZJNSjMxKT_JeuRAJ7E3WgtfKNNwUO_FBMRoc_hlpP6NbogfRGl7wPJ4Um4dEXJiq8AeW0UMTuYrWChuelW0rIYuUn8_Kogey3ZyD7TQ-XUzQG9MIlw6OfOO-cks36vgh_bvt28NrcnwKCuzN8WFZCIMwYzXGbfnNi6ZGYTo1kPLL-TkpmfQ4Wx3g5rpY8mpsPYC1m17DRgPJUs_j2i4O2f14aiEYC8zbBPGfbHzvSeuq69YQILaJ2ZKHR8M1B654OQXJAwGnk2Q96QUuL5KiikYzheiP4x-9MV1cf8TW2GXwrtq0ffgAAAAGuhmX6AA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Private_vcbot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/Rohan_Stock69") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/Rohan_Stock69") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("7223010810",)) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
