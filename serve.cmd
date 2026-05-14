@echo off
REM Always serve from the repo root (folder that contains _config.yml), not from subfolders like assets\vpython.
cd /d "%~dp0"
echo.
echo Jekyll site root: %CD%
echo Open http://127.0.0.1:4000 when ready.
echo.
bundle exec jekyll serve %*
