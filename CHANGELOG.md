# 변경 이력

이 파일의 형식은 [Keep a Changelog](https://keepachangelog.com/ko/1.1.0/) 를 따르고,
버전 번호는 [유의적 버전](https://semver.org/lang/ko/) 을 따릅니다.

## [Unreleased]

### Added
- 할 일을 검색하는 `find` 명령 (검토 중)

## [1.0.0] - 2026-09-17

첫 배포입니다. 할 일을 적고 끝내는 데 필요한 것만 담았습니다.

### Added
- `add` · `list` · `done` · `remove` 네 가지 명령
- 할 일을 `todo.json` 에 저장해 다시 켜도 남아 있게 함
- 설치 매뉴얼과 사용자 매뉴얼, 동작 구조 문서
- 기여 안내와 행동 규약

### Changed
- 목록 번호를 0 이 아니라 **1 부터** 세도록 함 — 사람이 세는 방식에 맞췄다

### Fixed
- 할 일이 하나도 없을 때 목록을 보면 오류가 나던 문제

[Unreleased]: https://github.com/SINGLE-COURSE-LECTURE/todo-cli-demo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/SINGLE-COURSE-LECTURE/todo-cli-demo/releases/tag/v1.0.0
