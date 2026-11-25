#!/usr/bin/env python3
"""Заготовка CLI для лабораторной работы.

Реализуйте подкоманды stats / train / detect / evaluate по контракту
из TASK.md (раздел «Контракт CLI»), затем замените этот файл.

Метод (zscore / iqr / knn / lof / ocsvm) и его параметры берутся из
config/config.yaml — см. свой вариант в config/variants.yaml.
"""

import sys


def main() -> int:
    print(
        "scripts/anomaly_cli.py пока не реализован. "
        "См. TASK.md, раздел «Контракт CLI».",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
