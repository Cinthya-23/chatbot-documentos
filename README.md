Chatbot Basado en PDF 

Este proyecto implementa un chatbot local que responde preguntas sobre el estudio de caso "HP Designjet Online: Un Éxito Espectacular", 
desarrollado por IESE Business School. El documento analiza en profundidad la estrategia de marketing relacional (CRM) aplicada por Hewlett-Packard (HP) 
para su división de impresoras de gran formato, detallando cómo el programa Designjet Online logró resultados sobresalientes en fidelización de clientes, 
eficiencia operativa, y participación de mercado.

A través de la vectorización semántica del contenido del PDF y la integración de un modelo de lenguaje local (`deepseek-r1:1.5b` vía Ollama), este chatbot 
permite explorar el contenido del paper mediante preguntas en lenguaje natural. La solución demuestra cómo la inteligencia artificial puede facilitar el 
acceso interactivo a documentos técnicos, con aplicaciones útiles en educación, negocios y análisis de casos empresariales reales.

Este trabajo forma parte de una práctica académica de construcción de agentes conversacionales basados en documentos, utilizando tecnologías libres y 
operativas en entorno local.

Estructura del Proyecto

chatbot-documentos/
│
├── paper.pdf # Documento base (PDF)
├── chatbot_embed_ollama.py # Script principal del chatbot
├── README.md # Este archivo


Requisitos

Antes de comenzar, asegúrate de tener instalado:

- [Python 3.9+]
- [Ollama] con el modelo: `deepseek-r1:1.5b`
- Git y GitHub Desktop (para gestionar repositorio)


Instalación de dependencias

Ejecuta en la terminal (CMD, Cursor, VSCode o Powershell):

bash
pip install sentence-transformers faiss-cpu PyMuPDF requests
ollama run deepseek-r1:1.5b

python chatbotpdf.py

Herramientas utilizadas
sentence-transformers

faiss
PyMuPDF
Ollama con el modelo deepseek-r1:1.5b
