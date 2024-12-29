import google.generativeai as genai
import youtube_transcript_api
from flask import jsonify
from core.config import API_KEY

genai.configure(api_key=API_KEY)

def mapper(data):
    return {
        "tipo_conteudo": data.get('tipoConteudo'),
        "conteudo": data.get('conteudo'),
        "quantidade_flashcard": data.get('quantidadeFlashcard'),
        "nivel_dificuldade": data.get('nivelDificuldade')
    }

def validacao_campos(dados):
    if int(dados['quantidade_flashcard']) < 5 or int(dados['quantidade_flashcard']) > 10:
        return jsonify({"error": "A quantidade de flashcards deve ser entre 5 e 10"}), 400
    if dados['tipo_conteudo'] != 'video' or dados['tipo_conteudo'] != 'texto':
        return jsonify({"error": "O tipo de conteúdo deve ser do tipo texto ou video"}), 400

def extrair_transcricao(video_url):
    video_id = video_url.split('v=')[1]
    try:
        transcricao = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])
    except youtube_transcript_api._errors.NoTranscriptFound:
        transcricao = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    texto = ' '.join([item['text'] for item in transcricao])
    return texto

def gerar_flashcards(texto, quantidade, dificuldade):
    prompt = f"Crie flashcards com perguntas e respostas baseadas no seguinte texto: {texto}. Gere {quantidade} flashcards com dificuldade {dificuldade}. Retorne as perguntas e respostas em formato de objeto JSON, onde a chave é a pergunta e o valor é a resposta."
    model = genai.GenerativeModel('gemini-pro')
    resposta = model.generate_content(prompt)
    return resposta.text


def main(data):
    mapperDados = mapper(data)
    validacao_campos(mapperDados)
    
    if mapperDados['tipo_conteudo'] == 'video':
        texto = extrair_transcricao(mapperDados['conteudo'])
        resposta = gerar_flashcards(texto, mapperDados['quantidade_flashcard'], mapperDados['nivel_dificuldade'])
        return jsonify({"flashcards": resposta}), 200

    if mapperDados['tipo_conteudo'] == 'texto': 
        resposta = gerar_flashcards(mapperDados['conteudo'], mapperDados['quantidade_flashcard'], mapperDados['nivel_dificuldade'])
        return jsonify({"flashcards": resposta}), 200
    
    else:
        return jsonify({"error": "Tipo de conteúdo inválido"}), 400