import smtplib 

servidor_email = smtplib.SMTP('smtp.gmail.com',587)

print(servidor_email.starttls())

servidor_email.login("')

remetente = 'isadoraaaalicia512@gmail.com'
destinatarios = ['brittobaptista93@gmail.com, isadoraaaalicia512@gmail.com, gleison.batista@prozeducacao.com.br']

conteudo = 'OIOIOI'

servidor_email.sendmail(remetente, destinatarios, conteudo)

servidor_email.quit()

