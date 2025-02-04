import matplotlib.pyplot as plt
import torch
from diffusers import FluxPipeline
import os

def gerar_imagem(pipe, descricao, output_path):
    # Geração da imagem
    image = pipe(
        prompt=descricao,
        guidance_scale=0.5,
        height=1360,
        width=768,
        num_inference_steps=15,
        max_sequence_length=256,
        generator=torch.Generator("cpu").manual_seed(0)
    ).images[0]

    # Exibir e salvar a imagem
    plt.imshow(image)
    plt.show()
    image.save(output_path)
    return output_path

def main():
    # Inicialização do pipeline
    pipe = FluxPipeline.from_pretrained(
        "----------------------------------------------------------", 
        torch_dtype=torch.bfloat16
    )
    pipe.enable_sequential_cpu_offload()
    Inicio = input("Deseja gerar uma nova persona (s/n)?\n")
    if Inicio == "n":
        print("Etapa de criação de nova persona pulada\n")
    else:
        print("Iniciando processo de geração de persona\n")
        while True:
            # Solicitar entrada do usuário
            descricao = input("Digite as características da persona que deseja criar com o nome fornecido:\n")
            arquivo = input("Digite o nome do arquivo de saída (sem extensão):\n").strip()
            arquivo = "------------------------------------------------------" + arquivo + ".jpg"

            # Caminho absoluto para o arquivo gerado
            output_dir = os.path.abspath(".")
            output_path = arquivo

            # Gerar a imagem
            print("Gerando a imagem...")
            gerar_imagem(pipe, descricao, output_path)

            # Perguntar ao usuário se deseja repetir
            repetir = input("Você está satisfeito com o resultado? (s/n):\n").strip().lower()
            if repetir == "s":
                print(f"A imagem foi salva em: {output_path}")
                break
            else:
                print("Reiniciando o processo de geração de persona\n")

if __name__ == "__main__":
    main()
