@echo off
rem Caminho do seu executável
set "exec_path=C:\VISUAL_RODOPAR\VISUAL_RODOPAR.exe"

rem Cria a chave de registro
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "VISUAL RODOPAR" /t REG_SZ /d "%exec_path%" /f

rem Exibe mensagem de sucesso
echo "Execucao automatica configurada com sucesso!"
pause
