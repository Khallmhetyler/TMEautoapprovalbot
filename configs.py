from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "16334231"))
    API_HASH = getenv("API_HASH", "54619d4b6d8a42602058d23d7815c6ea")
    BOT_TOKEN = getenv("BOT_TOKEN", "6018051026:AAFZJl4F1DZda1FN_9IEe3OdpY71HyyO0u8")
    FSUB = getenv("FSUB", "TylerMoviesEmpire")
    CHID = int(getenv("CHID", "-1001579762880"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Tyler:Umahpeters@cluster0.rtuol8u.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
