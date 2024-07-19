from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

def send_to_rabbitmq(reservation_details):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='reservations')
    channel.basic_publish(exchange='',
                          routing_key='reservations',
                          body=str(reservation_details))
    connection.close()

@app.route('/reserve', methods=['POST'])
def make_reservation():
    data = request.json
    # Aquí va la lógica de la reserva, por ejemplo, guardar en la base de datos
    # ...

    # Enviar detalles de la reserva a RabbitMQ
    send_to_rabbitmq(data)
    return jsonify({"status": "success", "message": "Reservation created successfully"})

if __name__ == '__main__':
    app.run(debug=True)
