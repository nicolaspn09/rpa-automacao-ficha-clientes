import apiibm
import time
import os
import mysql.connector
from datetime import datetime
import locale
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logExecucaoCodigos import grava_log_execucao_sql
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#Envia e-mail para os usuários
def envia_email(mensagemEmail, destinatarios_email, assunto_email):    
    # Configurações do servidor SMTP
    smtp_server = 'mail.COMPANY_NAME.com.br'
    smtp_port = 25  # Porta para comunicação segura com TLS

    # Credenciais do remetente
    remetente_email = "rpa@COMPANY_NAME.com.br"
    remetente_senha = 'REMOVED_FOR_GITHUB'

    destinatarios = destinatarios_email
    #destinatarios = [destinatarios_enviar]

    # Crie uma mensagem MIMEMultipart
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente_email
    mensagem['To'] = ",".join(destinatarios)
    mensagem['Subject'] = assunto_email

    # Adicione o corpo do e-mail
    corpo_email = mensagemEmail
    mensagem.attach(MIMEText(corpo_email, 'html'))  # 'plain' para texto simples ou 'html' para HTML

    try:
        pass # Logica de negocio removida por seguranca corporativa

def envia_email_execucao():
    pass # Logica de negocio removida por seguranca corporativa

def conecta_sql():
    pass # Logica de negocio removida por seguranca corporativa

def consulta_data():
    pass # Logica de negocio removida por seguranca corporativa

def diretorio_json():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela():
    pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql_insert(sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql(sql):
    pass # Logica de negocio removida por seguranca corporativa

def acessar_google_sheets():
    pass # Logica de negocio removida por seguranca corporativa
