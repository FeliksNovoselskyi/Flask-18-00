
"""
smtplib - библиотека для работы с SMTP

"smtp.gmail.com"


"""

import smtplib

# Создаем сессию для отправки письма
smtp_session = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
