@echo off
:: Python kurulu olmadan direk calistirmak icin
python lux_kar_hesaplama.py
if errorlevel 1 (
    echo Python bulunamadi. BUILD.bat ile once EXE olusturun.
    pause
)
