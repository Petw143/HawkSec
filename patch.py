def patch_file(file_path):
    try:
        # Abra o arquivo em modo binário e leia todos os bytes
        with open(file_path, "rb") as file:
            byt_file = bytearray(file.read())

        # Modifique os bytes na faixa especificada
        for i in range(0x423, 0x42D + 1):
            byt_file[i] = 0x90

        # Escreva os bytes modificados de volta ao arquivo
        with open(file_path, "wb") as file:
            file.write(byt_file)

        print("Alvo alterado com sucesso")

    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado")
    except IOError as e:
        print(f"Erro de I/O: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Caminho para o arquivo que será modificado, certifique-se que o caminho está correto.
file_path = "C:\\University\\HawkSec\\Fergonez\\5-Criando um Patcher\\fergonag.exe"

patch_file(file_path)
