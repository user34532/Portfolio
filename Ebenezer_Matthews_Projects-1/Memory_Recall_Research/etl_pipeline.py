import pandas as pd
from google.cloud import bigquery
import random
import matplotlib.pyplot as plt

# Simulate data extraction by generating random memory recall data
def generate_simulated_data(num_records):
    data = []
    for _ in range(num_records):
        participant_id = random.randint(1, 100)
        response_time = random.uniform(1.0, 3.5)
        total_recall = random.randint(5, 10)
        correct_recall = random.randint(0, total_recall)
        data.append([participant_id, response_time, total_recall, correct_recall])
    
    columns = ['participant_id', 'response_time', 'total_recall', 'correct_recall']
    return pd.DataFrame(data, columns=columns)

# Data analysis: Visualize memory recall accuracy
def plot_memory_recall_accuracy(data):
    data['recall_accuracy'] = data['correct_recall'] / data['total_recall']
    plt.hist(data['recall_accuracy'], bins=10, edgecolor='black')
    plt.title("Memory Recall Accuracy Distribution")
    plt.xlabel("Accuracy")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    data = generate_simulated_data(100)
    plot_memory_recall_accuracy(data)