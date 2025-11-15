from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import json
import os

app = Flask(__name__)
client = OpenAI(api_key="AQUI VA EL API KEY")

# Cargar productos
with open(r"D:\400-2\Comercio E\semana10Lab\chatbot\productos.json", "r", encoding="utf-8") as f:
    productos = json.load(f)

def buscar_producto(pregunta):
    pregunta = pregunta.lower()
    for p in productos:
        if p["nombre"].lower() in pregunta:
            return f"{p['nombre']} cuesta {p['precio']} soles y hay {p['stock']} unidades."
    return "No encontré ese producto en la tienda."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    info = buscar_producto(user_msg)

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un chatbot de tienda virtual."},
            {"role": "user", "content": f"Cliente pregunta: {user_msg}. Info: {info}"}
        ]
    )

    bot_msg = respuesta.choices[0].message.content
    return jsonify({"response": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
