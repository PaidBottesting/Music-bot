import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "d2d5ccf4592270fd54ad9e2014c960e7")
    BOT_TOKEN = os.environ.get("7385139018:AAH7Bou5YeNRKdxuwTAL1qeQ1Ynf62xRo5M",)
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIMBuygmnYpmxLBXiOTV6XwFWRLsrDm4tl28b9cL0q2jNSVzCps_ZdyAdcAJbxKJJnJb0WNsNi3CoMMYHM7itihgB2KsO4c9SDkE5E4I0e2MQftwDHbSLRDTXNn7HX4e8rcYKxnKp6su_HMHGr5JQcjE0bENrD4xS9h4WzVTxZtv6Iv19EIwfNSpkFkYQEvJ3dzHIdn7mJLSJG9zLMRsBoHEeM8BmCZxmPqT3pGPWkgCMwojPVt2_ihFOHfFe9APVI43rWSNsu72yPQv_mTeq5MPlN12wCTzPFhf4ga9IRLTmAcpd3iYzurptBY4FU0aHh2IHkyHVrXKjMLCg_xVPXfrqYs=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Zaid_01Musicbot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/Rohan_Stock69") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/Rohan_Stock69") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("7223010810", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
