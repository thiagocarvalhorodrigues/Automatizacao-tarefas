import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Email:

    def envia_email(self, destinatario, senha, email_remetente):
            corpo_email = "Prezado(a), \n\n" \
                          "Segue em anexo a tabela, com as vagas de TI em abertas na CADMUS;" \
                          "\n\nAtt;" \
                          "\n\n Thiago"

            try:
                fromaddr = email_remetente
                toaddr = destinatario
                msg = MIMEMultipart()
                msg['From'] = email_remetente
                msg['To'] = destinatario
                msg['Subject'] = "Vagas de TI abertas na CADMUS "
                body = corpo_email
                msg.attach(MIMEText(body, 'plain'))
                filename = 'thiago.xlsx'
                attachment = open('thiago.xlsx', 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(part)
                attachment.close()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_remetente, senha)
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
                server.quit()
                print('\n#####Email enviado com sucesso!#####')
                print('####Processo finalizado com sucesso####')
            except:
                print("Erro ao enviar")
