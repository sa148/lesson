# ログ出力 #
from Logging.config import getLogger, StreamHandler, DEBUG, ERROR

Logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
Logger.setLevel(DEBUG)
Logger.serLevel(handler)
Logger.debug('これはデバッグログです')

# ログフォーマット #
from Logging.config import getLogger, StreamHandler, DEBUG

formatter = Formatter('[%(levelname)s] %(asctime)s - %(messeage)s (%(filename)s)')
Logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormtter(formatter)
Logger.setLevel(DEBUG)
Logger.serLevel(handler)

Logger.debug('入力値は1000までです')
Logger.error('ファイルが存在していません')

