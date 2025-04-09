import PyPDF2
import random

def extrair_texto_pdf(caminho_pdf):
    """
    Extrai o texto de um arquivo PDF.
    """
    texto_completo = ""
    try:
        with open(caminho_pdf, "rb") as arquivo:
            leitor_pdf = PyPDF2.PdfReader(arquivo)
            for pagina in leitor_pdf.pages:
                texto_completo += pagina.extract_text()
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
    return texto_completo

def gerar_exercicios(texto, quantidade=100):
    """
    Gera uma lista de exercícios com base no texto fornecido.
    """
    frases = texto.split(".")  # Divide o texto em frases
    frases = [frase.strip() for frase in frases if len(frase.strip()) > 20]  # Remove frases curtas

    if len(frases) < quantidade:
        print("O texto não tem conteúdo suficiente para gerar todos os exercícios.")
        quantidade = len(frases)

    exercicios = []
    for i in range(quantidade):
        frase_base = random.choice(frases)
        exercicio = f"Exercício {i + 1}: {frase_base}"
        exercicios.append(exercicio)

    return exercicios

def salvar_exercicios(em_caminho, exercicios):
    """
    Salva os exercícios em um arquivo de texto.
    """
    try:
        with open(em_caminho, "w", encoding="utf-8") as arquivo:
            for exercicio in exercicios:
                arquivo.write(exercicio + "\n")
        print(f"Exercícios salvos em: {em_caminho}")
    except Exception as e:
        print(f"Erro ao salvar os exercícios: {e}")

# Caminho do arquivo PDF
caminho_pdf = input("Digite o caminho do arquivo PDF: ")

# Extrair texto do PDF
texto_extraido = extrair_texto_pdf(caminho_pdf)

# Verificar se o texto foi extraído
if texto_extraido.strip():
    # Gerar 100 exercícios
    exercicios_gerados = gerar_exercicios(texto_extraido, quantidade=100)

    # Salvar os exercícios em um arquivo de texto
    salvar_caminho = "exercicios_gerados.txt"
    salvar_exercicios(salvar_caminho, exercicios_gerados)
else:
    print("Não foi possível extrair texto do PDF.")
