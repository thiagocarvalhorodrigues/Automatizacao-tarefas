import re
from extrair import WebScraping
from emailer import Email

padrao_email = '\w{2,50}@\w{2,15}\.[a-z]{2,3}'

while True:
    destinatario = input(str('Informe o destinatário para o envio do relatório: '))
    validacao_email_destinatario = re.findall(padrao_email, destinatario)

    email_remetente = input(str('Informe o remetente do relatório: '))
    validacao_email_remetente = re.findall(padrao_email,email_remetente)
    senha = input(str('Informe a senha do e-mail: '))

    print("||||Aguarde, Montando a sua tabela.||||")
    if not validacao_email_destinatario:
        print(f'Email inválido!!\nPor favor insira um email válido [teste@exemplo.com]')
    elif not validacao_email_remetente:
        print(f'Email inválido!!\nPor favor insira um email válido [teste@exemplo.com]')
    else:
        break

obj = WebScraping()
obj.Iniciar()
enviar_email_planilha = Email()
enviar_email_planilha.envia_email(destinatario, senha, email_remetente)
