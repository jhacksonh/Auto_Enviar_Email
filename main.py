import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import time

class SMTPEnviarEmail:
    
    def __init__(self):
        load_dotenv()
        self.Iniciar_Envio()
        
    def Definir_Remetente(self):
        remetente = os.getenv("EMAIL_REMETENTE")  # Seu endereço de email
        senha = os.getenv("SENHA_DE_APP")  # sua Senha de App gerada pelo Google
        return remetente,senha
        
    def Manipular_Arquivos(self,arq, acao="r", dadoS=""):
        try:
            with open(arq, acao, encoding='utf-8') as arquivo:
                if acao == "r":
                    return [dadoS.rstrip('\n') for dadoS in arquivo.readlines()]
                arquivo.write(dadoS)
                return dadoS
        except Exception as e:
            print(f"Erro ao {'ler' if acao == 'r' else 'escrever'}: {e}")

    def Enviar_Email(self,destinatario, assunto, mensagem):
        remetente,senha = self.Definir_Remetente()
        try:
            # Configurar a mensagem
            msg = MIMEMultipart()
            msg['From'] = remetente
            msg['To'] = destinatario
            msg['Subject'] = assunto
            msg.attach(MIMEText(mensagem, 'plain'))

            # Conectar ao servidor SMTP
            servidor = smtplib.SMTP('smtp.gmail.com', 587)
            servidor.starttls()  # Inicia a conexão segura
            servidor.login(remetente, senha)
            servidor.sendmail(remetente, destinatario, msg.as_string()) #envia 
            print(f"Email enviado com sucesso para: {destinatario}! ")

            servidor.quit()

        except Exception as e:
            print(f"Erro ao enviar email: {e}")

    def Iniciar_Envio(self):
        destinatarios = self.Manipular_Arquivos('destinatarios.txt')# puxa os dados do txt
        for destino in destinatarios: # ler os dados
            nome = destino.split('|')[0] # pega nome
            email = destino.split('|')[1] # pega email
            print(f"Enviando Email para {nome}...")
            time.sleep(.5) # envia a cada meio segundo
            self.Enviar_Email(
                destinatario=email,
                assunto="--Define o título (do que se trata o E-mail)--",
                mensagem=f"""Olá {nome}, --Descreve o contexto da mensagem--"""
            )
            
SMTPEnviarEmail()