#!/usr/bin/env python3
"""termcheck.py - 문서에서 쓰지 않기로 한 말을 찾는다.

사용법:
    python tools/termcheck.py docs README.md

사전은 tools/terms.json 에 있다. 하나라도 걸리면 종료 코드 1 로 끝난다.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS = os.path.join(HERE, "terms.json")


def md_files(paths):
    for path in paths:
        if os.path.isfile(path) and path.endswith(".md"):
            yield path
        for root, _dirs, names in os.walk(path):
            for name in sorted(names):
                if name.endswith(".md"):
                    yield os.path.join(root, name)


def main(argv):
    paths = argv[1:] or ["docs"]
    with open(TERMS, encoding="utf-8") as f:
        terms = json.load(f)["terms"]

    hits = 0
    for path in md_files(paths):
        with open(path, encoding="utf-8") as f:
            for no, line in enumerate(f, 1):
                for bad, good in terms.items():
                    if bad in line:
                        hits += 1
                        print("!! %s:%d: '%s' 대신 '%s' 를 씁니다" % (path, no, bad, good))

    print()
    print("걸린 표현 %d개" % hits)
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
