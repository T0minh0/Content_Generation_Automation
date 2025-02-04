@echo off

REM 1. Ativar o ambiente conda do programa Geracao_Educado_final.py (FLUX)
call conda activate FLUX
if errorlevel 1 (
    echo Erro ao ativar o ambiente FLUX. Certifique-se de que ele está configurado corretamente.
    exit /b 1
)

REM 2. Executar o programa Geracao_Educado_final.py com stdout imediato
python -u "C:\Users\boris\AI\Flux\codes\flix1schnell\Geracao_Educado_final.py"
if errorlevel 1 (
    echo Erro ao executar o programa Geracao_Educado_final.py.
    exit /b 1
)

REM 3. Desativar o ambiente FLUX
call conda deactivate

REM 4. Ativar o ambiente conda do programa TTS_masc.py (TTS)
call conda activate TTS
if errorlevel 1 (
    echo Erro ao ativar o ambiente TTS. Certifique-se de que ele está configurado corretamente.
    exit /b 1
)

REM 5. Executar o programa TTS_masc.py com stdout imediato
python -u "C:\Users\boris\AI\Coqui\TTS_masc.py"
if errorlevel 1 (
    echo Erro ao executar o programa TTS_masc.py.
    exit /b 1
)

REM 6. Desativar o ambiente TTS
call conda deactivate

REM 7. Ativar o ambiente conda do programa inference.py (SADT)
call conda activate SADT
if errorlevel 1 (
    echo Erro ao ativar o ambiente SADT. Certifique-se de que ele está configurado corretamente.
    exit /b 1
)

REM 8. Executar o programa inference.py com stdout imediato
python -u "C:\Users\boris\AI\SAD\SadTalker\Final_Aula_Educado.py" --still --preprocess full --enhancer gfpgan
if errorlevel 1 (
    echo Erro ao executar o programa inference.py.
    exit /b 1
)

REM 9. Desativar o ambiente SADT
call conda deactivate

pause