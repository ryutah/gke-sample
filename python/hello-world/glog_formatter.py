import time

from logging import DEBUG, INFO, WARN, ERROR, CRITICAL
from logging import Formatter
from logging import LogRecord

from math import modf


LOG_LEVEL_MAP = {
    DEBUG: "D",
    INFO: "I",
    WARN: "W",
    ERROR: "E",
    CRITICAL: "C",
}
"""Glogログレベル ログレベルナンバーとマッピングさせる"""


class GlogFormatter(Formatter):
    """Glog 形式でログを出力するフォーマッタ

    ログフォーマット:
        Lmmdd hh:mm:ss.uuuuuu threadid file:line] msg...
    フィールドについて
        L               エラーレベル
        mm              月(2桁)
        dd              日(2桁)
        hh:mm:ss.uuuuuu 時(2桁):分(2桁):秒(2桁).秒の小数部(6桁)
        threadid        スレッドID(7桁)
        file            ファイル名
        line            行番号
        msg             ログメッセージ
    """

    def __init__(self):
        Formatter.__init__(self)

    def format(self, record: LogRecord) -> str:
        # ログレベルの設定 不明なログレベルの場合は "?" で出力
        level = LOG_LEVEL_MAP[record.levelno] if record.levelno in LOG_LEVEL_MAP.keys() else "?"

        # ログ出力日時を日付型に変換
        create_time = time.localtime(record.created)
        # ログ出力日時の小数部取得
        ftime = int(modf(record.created)[0] * 1e6)

        msg = "{level}{month:02d}{date:02d} {hour:02d}:{min:02d}:{sec:02d}.{fsec:06d} {tid:7} {file}:{line}] {msg}".format(
            level=level, month=create_time.tm_mon, date=create_time.tm_mday, hour=create_time.tm_hour,
            min=create_time.tm_min, sec=create_time.tm_sec, fsec=ftime, tid=record.process, file=record.filename,
            line=record.lineno, msg=record.getMessage(),
        )
        return msg
