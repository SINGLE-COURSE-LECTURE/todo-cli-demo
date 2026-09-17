@echo off
rem check.bat - 문서 검사 네 가지를 한 번에 돌린다. 하나라도 실패하면 1 로 끝난다.
setlocal
set FAIL=0
set DOCS=docs README.md CONTRIBUTING.md CHANGELOG.md CODE_OF_CONDUCT.md

echo == 1. 형식 ==
pymarkdown scan %DOCS%
if errorlevel 1 set FAIL=1

echo.
echo == 2. 사이트 빌드 (경고를 실패로) ==
mkdocs build --strict -q --site-dir .site-check 2> .site-check.log
if errorlevel 1 set FAIL=1
type .site-check.log

echo.
echo == 3. 바깥 주소 ==
python tools\linkcheck.py -q %DOCS%
if errorlevel 1 set FAIL=1

echo.
echo == 4. 용어 ==
python tools\termcheck.py %DOCS%
if errorlevel 1 set FAIL=1

echo.
if "%FAIL%"=="0" (echo 전부 통과) else (echo 실패한 검사가 있습니다)
exit /b %FAIL%
