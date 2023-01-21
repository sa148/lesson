# ログ出力 #
from Logging import getLogger, StreamHandler, DEBUG

Logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
Logger.setLevel(DEBUG)
Logger.serLevel(handler)
Logger.debug('これはデバッグログです')