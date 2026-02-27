@echo off
title Lux Mallar - EXE Builder
color 0A
echo.
echo  ============================================
echo   LUX MALLAR KAR HESAPLAMA - EXE BUILDER
echo  ============================================
echo.

:: Python kontrol
python --version >nul 2>&1
if errorlevel 1 (
    echo  [HATA] Python bulunamadi!
    echo  Python indirmek icin: https://www.python.org/downloads/
    echo  Kurulumda "Add Python to PATH" secenegini isaretleyin!
    pause
    exit /b 1
)

echo  [OK] Python bulundu.
echo.

:: pip ile pyinstaller kur
echo  [1/3] PyInstaller kuruluyor...
pip install pyinstaller --quiet
if errorlevel 1 (
    echo  [HATA] PyInstaller kurulamadi. Internet baglantinizi kontrol edin.
    pause
    exit /b 1
)
echo  [OK] PyInstaller hazir.
echo.

:: EXE olustur
echo  [2/3] EXE olusturuluyor (1-2 dakika surebilir)...
pyinstaller ^
    --onefile ^
    --windowed ^
    --name "LuxMallarKarHesaplama" ^
    --icon=NONE ^
    --clean ^
    lux_kar_hesaplama.py

if errorlevel 1 (
    echo  [HATA] EXE olusturulamadi!
    pause
    exit /b 1
)

echo.
echo  [3/3] Temizlik yapiliyor...
rmdir /s /q build >nul 2>&1
del /q *.spec >nul 2>&1

echo.
echo  ============================================
echo   BASARILI! EXE dosyasi:
echo   dist\LuxMallarKarHesaplama.exe
echo  ============================================
echo.
echo  EXE dosyasini istediginiz yere kopyalayabilirsiniz.
echo  Python kurulu olmayan bilgisayarlarda da calisir!
echo.
pause
