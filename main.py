#Módulo ejecutable para suscribirse a eventos y mostrar los datos actualizados:
# main.py
from datamanager import RealTimeDataManager
from eventos import EventManager
import threading
import time

def callback_mostrar_datos_actualizados(data):
    print(f'Datos en tiempo real actualizados: {data}')

if __name__ == "__main__":
    real_time_data_manager = RealTimeDataManager()
    event_manager = real_time_data_manager.event_manager

    # Suscribe el callback al evento de actualización de datos
    event_manager.subscribe("actualizacion_datos", callback_mostrar_datos_actualizados)

    # Inicia el hilo de actualización en tiempo real
    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEl rograma ha finalizado.")
