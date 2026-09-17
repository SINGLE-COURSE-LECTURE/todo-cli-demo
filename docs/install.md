# 설치 매뉴얼

`todo` 를 내 컴퓨터에서 실행되게 만드는 데까지 안내합니다. **10분** 이면 됩니다.

## 1. 누가 읽는 문서인가

- 터미널(명령 프롬프트)을 **처음 써 보는 분**도 따라 할 수 있게 썼습니다
- 윈도우 10·11 기준입니다. macOS 는 3-2 를 보세요

## 2. 먼저 있어야 하는 것

| 필요한 것 | 확인하는 방법 | 없다면 |
|---|---|---|
| 파이썬 3.8 이상 | `python --version` | [python.org](https://www.python.org/downloads/) 에서 내려받기 |
| Git | `git --version` | [git-scm.com](https://git-scm.com/downloads) 에서 내려받기 |

## 3. 설치하기

### 3-1. 윈도우

**① 터미널을 엽니다**

시작 단추 옆 검색 칸에 `cmd` 라고 치고 **명령 프롬프트**를 엽니다.

**② 파이썬이 있는지 봅니다**

```bash
python --version
```

`Python 3.12.1` 처럼 숫자가 나오면 됩니다.

**③ 내려받습니다**

```bash
git clone https://github.com/SINGLE-COURSE-LECTURE/todo-cli-demo.git
```

**④ 폴더로 들어갑니다**

```bash
cd todo-cli-demo
```

**⑤ 실행되는지 봅니다**

```bash
python todo.py list
```

`할 일이 없습니다.` 가 나오면 **설치가 끝난 것**입니다.

### 3-2. macOS · 리눅스

같은 순서이고 `python` 대신 **`python3`** 를 씁니다.

```bash
git clone https://github.com/SINGLE-COURSE-LECTURE/todo-cli-demo.git
cd todo-cli-demo
python3 todo.py list
```

## 4. 잘 됐는지 확인하기

```bash
python todo.py add "설치 확인"
python todo.py list
```

`1. [ ] 설치 확인` 이 보이면 정상입니다. 확인이 끝났으면 지웁니다.

```bash
python todo.py remove 1
```

## 5. 막혔을 때

| 이렇게 나오면 | 뜻 | 이렇게 하세요 |
|---|---|---|
| `'python'은(는) 내부 또는 외부 명령...` | 파이썬이 없거나 경로에 없다 | 파이썬을 다시 설치하되 **Add python.exe to PATH** 를 체크 |
| `'git'은(는) 내부 또는 외부 명령...` | Git 이 없다 | Git 을 설치하고 **터미널을 닫았다 다시** 엽니다 |
| `No such file or directory: 'todo.py'` | 폴더 밖에 있다 | `cd todo-cli-demo` 를 했는지 확인 |
| 한글이 깨져 보인다 | 터미널 글자 설정 | `chcp 65001` 을 한 번 실행 |

## 6. 지우기

폴더를 통째로 지우면 끝납니다. 레지스트리나 다른 곳에 남기는 것이 없습니다.

## 7. 다음에 볼 문서

- [사용자 매뉴얼](usage.md) — 네 가지 명령 사용법
