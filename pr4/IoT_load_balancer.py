import random
import time
import threading
from queue import Queue

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class IoTSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def generate_data(self):
        """Генерує випадкові дані про споживання енергії."""
        return {
            'sensor_id': self.sensor_id,
            'energy_usage': random.uniform(0.5, 5.0),  # Випадкове споживання енергії
            'timestamp': time.time()
        }


class ProcessingNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.queue = Queue()
        self.processing_time = random.uniform(0.1, 0.5)  # Час обробки запиту
        self.processed_count = 0  # Лічильник оброблених запитів

    def process_data(self):
        while True:
            data = self.queue.get()
            if data is None:
                break  # Вихідний сигнал для завершення
            time.sleep(self.processing_time)  # Симуляція обробки
            self.processed_count += 1
            print(f"Node {self.node_id} processed data from Sensor {data['sensor_id']}")
            self.queue.task_done()


class LoadBalancer:
    def __init__(self, nodes, strategy='round_robin'):
        self.nodes = nodes
        self.strategy = strategy
        self.counter = 0

    def distribute(self, data):
        if self.strategy == 'round_robin':
            node = self.nodes[self.counter % len(self.nodes)]
            self.counter += 1
        elif self.strategy == 'least_response_time':
            node = min(self.nodes, key=lambda n: n.queue.qsize())
        node.queue.put(data)


# Створення вузлів обробки
total_nodes = 3
nodes = [ProcessingNode(i) for i in range(total_nodes)]

# Запуск обробників у потоках
for node in nodes:
    threading.Thread(target=node.process_data, daemon=True).start()

# Балансувальник навантаження
balancer = LoadBalancer(nodes, strategy='round_robin')

# Симуляція датчиків
total_sensors = 5
sensors = [IoTSensor(i) for i in range(total_sensors)]

for _ in range(20):  # Симуляція 20 ітерацій збору даних
    sensor = random.choice(sensors)
    data = sensor.generate_data()
    balancer.distribute(data)
    time.sleep(random.uniform(0.1, 0.3))  # Імітація нерегулярних запитів

# Побудова графіка розподілу навантаження
node_ids = [node.node_id for node in nodes]
processed_counts = [node.processed_count for node in nodes]

plt.bar(node_ids, processed_counts, color='skyblue')
plt.xlabel("Node ID")
plt.ylabel("Processed Requests")
plt.title("Load Distribution Among Processing Nodes")
plt.show()
