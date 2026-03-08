import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import schedule
import time


def gerar_relatorio_e_enviar():
    try:
        df = pd.read_excel('dados_semanais.xlsx', sheet_name='Sheet1')
    except FileNotFoundError:
        print("Arquivo não encontrado. Certifique-se de que 'dados_semanais.xlsx' existe.")
        return

    df = df.dropna()
    
    if 'Data' in df.columns:
        df['Data'] = pd.to_datetime(df['Data'])
    
    hoje = datetime.date.today()
    inicio_semana = hoje - datetime.timedelta(days=hoje.weekday())
    df_semanal = df[df['Data'].dt.date >= inicio_semana] if 'Data' in df.columns else df

    if 'Categoria' in df_semanal.columns and 'Valor' in df_semanal.columns:
        relatorio = df_semanal.groupby('Categoria')['Valor'].agg(['sum', 'mean', 'count']).reset_index()
        relatorio.columns = ['Categoria', 'Soma', 'Média', 'Contagem']
    else:
        relatorio = df_semanal

    arquivo_relatorio = 'relatorio_semanal.xlsx'
    relatorio.to_excel(arquivo_relatorio, index=False)

    remetente = 'seu_email@example.com'
    senha = 'sua_senha'
    destinatario = 'destinatario@example.com'
    servidor_smtp = 'smtp.gmail.com'
    porta = 587

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = f'Relatório Semanal - {hoje.strftime("%Y-%m-%d")}'

    corpo = 'Olá,\n\nSegue em anexo o relatório semanal gerado automaticamente.\n\nAtenciosamente,\nSeu Script Python'
    msg.attach(MIMEText(corpo, 'plain'))

    with open(arquivo_relatorio, 'rb') as f:
        anexo = MIMEApplication(f.read(), _subtype='xlsx')
        anexo.add_header('Content-Disposition', 'attachment', filename=arquivo_relatorio)
        msg.attach(anexo)

    try:
        server = smtplib.SMTP(servidor_smtp, porta)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

schedule.every().monday.at("09:00").do(gerar_relatorio_e_enviar)

while True:
    schedule.run_pending()
    time.sleep(60)
