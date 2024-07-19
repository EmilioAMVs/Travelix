import pika
import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'r20003848@gmail.com'
    msg['To'] = to_address

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('r20003848@gmail.com', 'jcsb jdks whbe opdn')
        server.sendmail('r20003848@gmail.com', to_address, msg.as_string())

def callback(ch, method, properties, body):
    reservation_details = body.decode()
    # Procesar los detalles de la reserva y enviar correo electrónico
    send_email('destinatario@example.com', 'Detalles de tu reserva', reservation_details)

credentials = pika.PlainCredentials('administrator', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='reservations')
channel.basic_consume(queue='reservations', on_message_callback=callback, auto_ack=True)

print('Esperando mensajes...')
channel.start_consuming()
