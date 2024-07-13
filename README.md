# Resolução do exercício proposto pelo Fergonez

# Introdução

Essa é uma documentação da análise feita pelo Fergonez (disponível em [Fergonez](https://www.fergonez.net/engrev/engrev5)).

Esse código foi desenvolvido usando como base o código escrito pelo Fergonez no link disponibilizado anteriormente. Porém, foi escrito na linguagem Python.

# Passo-a-passo

**Passo a passo para alterar o arquivo executável:**

1. **Defina a função `patch_file`:**
    ```python
    def patch_file(file_path):
    ```

2. **Abra o arquivo em modo binário e leia todos os bytes:**
    ```python
    try:
        with open(file_path, "rb") as file:
            byt_file = bytearray(file.read())
    ```

3. **Modifique os bytes na faixa especificada:**
    ```python
        for i in range(0x423, 0x42D + 1):
            byt_file[i] = 0x90
    ```

4. **Escreva os bytes modificados de volta ao arquivo:**
    ```python
        with open(file_path, "wb") as file:
            file.write(byt_file)
    ```

5. **Imprima uma mensagem de sucesso:**
    ```python
        print("Alvo alterado com sucesso")
    ```

6. **Trate possíveis erros:**
    ```python
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado")
    except IOError as e:
        print(f"Erro de I/O: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    ```

7. **Especifique o caminho para o arquivo que será modificado:**
    ```python
    file_path = "C:\\University\\HawkSec\\Fergonez\\5-Criando um Patcher\\fergonag.exe"
    ```

8. **Chame a função `patch_file`:**
    ```python
    patch_file(file_path)
    ```

Aqui está o código completo:

```python
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

``` 

# Creditos 

O código foi desenvolvido pelo Pedro, e a análise na qual eu me baseei foi feita pelo Fergonez (disponível em [Fergonez]).