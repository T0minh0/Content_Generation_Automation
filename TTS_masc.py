from TTS.api import TTS  # type: ignore
import os

def main():
    # Inicializa o modelo TTS
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

    # Solicita entrada do usuário
    path = input("Digite o nome do curso:\n").strip()
    path = "C:\\Users\\boris\\AI\\SAD\\SadTalker\\Source\\audio\\" + path + ".wav"

    texto = input("Digite o roteiro:\n").strip()

    # Gera o áudio com o texto fornecido
    tts.tts_to_file(
        text=texto,
        file_path=path,
        speaker_wav="C:\\Users\\boris\\AI\\Coqui\\Origens\\base_voz_3h.wav",
        language="pt",
        split_sentences=True
    )

    # Retorna o caminho absoluto do arquivo gerado
    output_path = os.path.abspath(path)
    print(output_path)

if __name__ == "__main__":
    main()