import fitz  # PyMuPDF
import numpy as np
import faiss
import requests
from sentence_transformers import SentenceTransformer

# === CONFIGURACIÓN ===
pdf_path = r"C:\Users\HP\Documents\GitHub\chatbot-documentos\Occasional Paper.pdf"  # AJUSTA si renombraste
ollama_model = "deepseek-r1:1.5b"

# === 1. Extraer texto desde PDF ===
def extraer_texto_pdf(ruta_pdf):
    documento = fitz.open(ruta_pdf)
    paginas = []
    for pagina in documento:
        texto = pagina.get_text().strip()
        if texto:
            paginas.append(texto)
    return paginas

# === 2. Crear embeddings ===
def generar_embeddings(lista_textos):
    modelo = SentenceTransformer("all-MiniLM-L6-v2")
    vectores = modelo.encode(lista_textos, show_progress_bar=True)
    return modelo, vectores

# === 3. Crear índice FAISS ===
def construir_faiss(vectores):
    indice = faiss.IndexFlatL2(vectores.shape[1])
    indice.add(vectores)
    return indice

# === 4. Llamado al modelo en Ollama ===
def consultar_ollama(contexto, pregunta):
    prompt = f"""Responde basándote en el siguiente contexto del documento:

\"\"\"
{contexto}
\"\"\"

Pregunta: {pregunta}
Respuesta:"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": ollama_model,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# === 5. Bucle conversacional ===
def modo_chatbot(fragmentos, vectores, indice, modelo_embed):
    print("\n🧠 Chatbot DeepSeek listo. Escribe 'salir' para terminar.")
    while True:
        pregunta = input("\n💬 Tu pregunta: ")
        if pregunta.lower() in ["salir", "exit", "quit"]:
            print("👋 Hasta luego.")
            break

        pregunta_vec = modelo_embed.encode([pregunta])
        _, idxs = indice.search(np.array(pregunta_vec), k=3)
        contexto = "\n---\n".join([fragmentos[i] for i in idxs[0]])

        respuesta = consultar_ollama(contexto, pregunta)
        print("\n📄 Respuesta del modelo:")
        print(respuesta)

# === EJECUCIÓN ===

print("📖 Leyendo PDF...")
fragmentos = extraer_texto_pdf(pdf_path)

print("🔎 Generando embeddings...")
modelo_embed, vectores = generar_embeddings(fragmentos)

print("📦 Construyendo índice semántico...")
indice = construir_faiss(np.array(vectores))

modo_chatbot(fragmentos, vectores, indice, modelo_embed)
