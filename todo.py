#!/usr/bin/env python3
"""todo - 한 줄짜리 할 일 관리 도구.

사용법:
    python todo.py add "장보기"
    python todo.py list
    python todo.py done 1
    python todo.py remove 1
"""
import json
import os
import sys

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo.json")


def load():
    if not os.path.exists(DATA):
        return []
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def save(items):
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def cmd_add(args):
    if not args:
        print("할 일 내용을 적어 주세요.  예) python todo.py add \"장보기\"")
        return 1
    items = load()
    items.append({"text": " ".join(args), "done": False})
    save(items)
    print("추가했습니다: %s" % items[-1]["text"])
    return 0


def cmd_list(args):
    items = load()
    if not items:
        print("할 일이 없습니다.")
        return 0
    for i, it in enumerate(items, 1):
        print("%d. [%s] %s" % (i, "x" if it["done"] else " ", it["text"]))
    return 0


def pick(items, args):
    if not args or not args[0].isdigit():
        print("번호를 적어 주세요.  예) python todo.py done 1")
        return None
    n = int(args[0])
    if not 1 <= n <= len(items):
        print("1 부터 %d 사이의 번호를 적어 주세요." % len(items))
        return None
    return n - 1


def cmd_done(args):
    items = load()
    i = pick(items, args)
    if i is None:
        return 1
    items[i]["done"] = True
    save(items)
    print("끝냈습니다: %s" % items[i]["text"])
    return 0


def cmd_remove(args):
    items = load()
    i = pick(items, args)
    if i is None:
        return 1
    gone = items.pop(i)
    save(items)
    print("지웠습니다: %s" % gone["text"])
    return 0


COMMANDS = {"add": cmd_add, "list": cmd_list, "done": cmd_done, "remove": cmd_remove}


def main(argv):
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print(__doc__.strip())
        return 1
    return COMMANDS[argv[1]](argv[2:])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
