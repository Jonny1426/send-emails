import smtplib
from email.mime.text import MIMEText


email_de_envio = input('Email de envio: ')
senha = input('senha: ')
assinatura = input('Assinatura: ')
assunto = input('Assunto: ')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_de_envio, senha)

destinatarios = open('destinatarios.txt', 'r')
dest_list = destinatarios.readlines()

for dest in dest_list:
    try:
        para = dest
        msg = MIMEText(open('email.txt', 'r').read())
        msg['From'] = assinatura
        msg['Subject'] = assunto

        msg = msg.as_string()
    
        server.sendmail(email_de_envio, para, msg)
    
        print(f'Mensagem enviada com sucesso para {dest}')

    except Exception as e:
        print('erro: ', e)
    

server.quit()
print('Requisição finalizada')
