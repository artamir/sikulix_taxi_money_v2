title=siculix_starter
cd .
:loop

call Siculix_taxi_run.bat
TIMEOUT /T 3
taskkill /IM firefox.exe /F


goto loop