start cmd /k "python preproc.py"

:wait
ping -n 1 127.0.0.1 > NUL
if exist "%ERRORLEVEL%" (
  goto wait
)

echo Flask server is ready!
