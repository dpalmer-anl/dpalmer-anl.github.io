@echo off
REM Always serve from the repo root (folder that contains _config.yml).
REM If you run `jekyll serve` or `bundle exec jekyll serve` from e.g. `scripts\`, Jekyll uses that
REM folder as the site source and you will see a directory listing of Python files instead of the site.
cd /d "%~dp0"
if not exist "_config.yml" (
  echo ERROR: _config.yml not found in %CD%
  echo Run this script from the Jekyll repository root ^(the folder that contains _config.yml^).
  exit /b 1
)
echo.
echo Jekyll site root: %CD%
echo Open http://127.0.0.1:4000 when ready.
echo.
bundle exec jekyll serve %*
