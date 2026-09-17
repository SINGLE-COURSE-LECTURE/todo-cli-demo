#!/usr/bin/env python3
"""linkcheck.py - 문서에 적힌 바깥 주소가 정말 열리는지 두드려 본다.

사용법:
    python tools/linkcheck.py docs README.md
    python tools/linkcheck.py -q docs       # 실패한 것만 보여 준다

하나라도 열리지 않으면 종료 코드 1 로 끝난다.
"""
import os
import re
import sys
import urllib.error
import urllib.request

LINK = re.compile(
    r"\]\((https?://[^)\s]+)\)"        # [글자](주소)
    r"|<(https?://[^>\s]+)>"           # <주소>
    r"|^\s*\[[^\]]+\]:\s*(https?://\S+)"  # [이름]: 주소  (참조 방식)
)
SKIP_PREFIX = ("https://img.shields.io/",)
TIMEOUT = 10
AGENT = "Mozilla/5.0 (docs-linkcheck)"


def md_files(paths):
    for path in paths:
        if os.path.isfile(path) and path.endswith(".md"):
            yield path
        for root, _dirs, names in os.walk(path):
            for name in sorted(names):
                if name.endswith(".md"):
                    yield os.path.join(root, name)


def collect(paths):
    found = {}
    for path in md_files(paths):
        with open(path, encoding="utf-8") as f:
            for no, line in enumerate(f, 1):
                for m in LINK.finditer(line):
                    url = m.group(1) or m.group(2) or m.group(3)
                    found.setdefault(url, []).append("%s:%d" % (path, no))
    return found


def check(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as res:
            return res.status
    except urllib.error.HTTPError as e:
        if e.code in (403, 405):  # HEAD 를 막는 서버는 GET 으로 다시
            try:
                req = urllib.request.Request(url, headers={"User-Agent": AGENT})
                with urllib.request.urlopen(req, timeout=TIMEOUT) as res:
                    return res.status
            except Exception as e2:
                return getattr(e2, "code", str(e2))
        return e.code
    except Exception as e:
        return str(e)


def main(argv):
    args = argv[1:]
    quiet = "-q" in args or "--quiet" in args
    paths = [a for a in args if not a.startswith("-")] or ["docs"]
    found = collect(paths)
    if not found:
        print("검사할 바깥 주소가 없습니다.")
        return 0

    bad = 0
    for url in sorted(found):
        if url.startswith(SKIP_PREFIX):
            if not quiet:
                print("SKIP %-60s 건너뜀(배지)" % url[:60])
            continue
        status = check(url)
        if status == 200:
            if not quiet:
                print("OK   %-60s %s" % (url[:60], status))
        else:
            bad += 1
            print("!!   %-60s %s" % (url[:60], status))
            for where in found[url]:
                print("     %s" % where)

    print()
    print("주소 %d개 · 실패 %d개" % (len(found), bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
