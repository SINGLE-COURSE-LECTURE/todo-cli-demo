# 사용자 매뉴얼

`todo` 로 **할 수 있는 일**을 하나씩 안내합니다. 설치가 아직이면 [설치 매뉴얼](install.md) 을 먼저 보세요.

![todo 를 터미널에서 실행해 할 일을 더하고 목록을 보고 하나를 끝낸 화면](assets/todo-usage.png)

## 할 일을 적고 싶다

```bash
python todo.py add "장보기"
```

```text
추가했습니다: 장보기
```

띄어쓰기가 있는 내용은 **큰따옴표로 묶습니다.** 묶지 않아도 동작하지만 습관을 들이는 편이 낫습니다.

## 지금 뭐가 남았는지 보고 싶다

```bash
python todo.py list
```

```text
1. [x] 장보기
2. [ ] 교재 3장 읽기
```

- 앞의 **숫자**가 그 할 일의 번호입니다. `done` · `remove` 는 이 번호를 씁니다
- `[x]` 는 끝난 것, `[ ]` 는 아직인 것입니다

## 끝냈다고 표시하고 싶다

```bash
python todo.py done 1
```

```text
끝냈습니다: 장보기
```

## 목록에서 지우고 싶다

```bash
python todo.py remove 1
```

```text
지웠습니다: 장보기
```

> **주의** — 지우면 되돌릴 수 없습니다. 끝난 일을 기록으로 남기고 싶다면 `remove` 대신 `done` 을 쓰세요.

## 다른 컴퓨터에서 이어서 쓰고 싶다

할 일은 프로그램과 **같은 폴더의 `todo.json`** 파일에 들어 있습니다.
이 파일 하나만 옮기면 그대로 이어집니다.

## 자주 묻는 것

자세한 내용은 [없는 문서](https://github.com/SINGLE-COURSE-LECTURE/todo-cli-demo/blob/main/NOPE.md) 를 보세요.

| 묻는 것 | 답 |
|---|---|
| 번호를 잘못 눌러 지웠어요 | 되돌릴 수 없습니다. `todo.json` 을 미리 복사해 두면 안전합니다 |
| 할 일이 몇 개까지 되나요 | 제한이 없습니다. 다만 백 개가 넘으면 목록이 길어 보기 불편합니다 |
| 끝낸 일만 모아 보고 싶어요 | 아직 안 됩니다. [변경 이력][changelog] 의 `Unreleased` 에서 검토 중입니다 |
| 마감 날짜를 넣고 싶어요 | 아직 안 됩니다. 필요하시면 이슈로 알려 주세요 |

## 다음에 볼 문서

- [동작 구조](architecture.md) — 안에서 무슨 일이 일어나는지

[changelog]: https://github.com/SINGLE-COURSE-LECTURE/todo-cli-demo/blob/main/CHANGELOG.md
