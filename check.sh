#!/bin/bash
# check.sh - 문서 검사 네 가지를 한 번에 돌린다. 하나라도 실패하면 1 로 끝난다.
fail=0
docs="docs README.md CONTRIBUTING.md CHANGELOG.md CODE_OF_CONDUCT.md"

echo "== 1. 형식 =="
pymarkdown scan $docs || fail=1

echo
echo "== 2. 사이트 빌드 (경고를 실패로) =="
mkdocs build --strict --site-dir .site-check || fail=1

echo
echo "== 3. 바깥 주소 =="
python tools/linkcheck.py $docs || fail=1

echo
echo "== 4. 용어 =="
python tools/termcheck.py $docs || fail=1

echo
if [ "$fail" -eq 0 ]; then echo "전부 통과"; else echo "실패한 검사가 있습니다"; fi
exit $fail
