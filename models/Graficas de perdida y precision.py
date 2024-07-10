import matplotlib.pyplot as plt

# Datos del nuevo entrenamiento
epochs = list(range(1, 11))
train_loss = [1.2997, 0.6387, 0.5915, 0.5907, 0.5575, 0.5299, 0.5123, 0.5080, 0.4954, 0.4880]  # Ajuste para 10 epochs
val_loss = [0.6446, 0.6528, 0.6208, 0.6476, 0.6293, 0.6232, 0.6138, 0.6174, 0.6295, 0.7310]
train_acc = [0.6034, 0.6456, 0.7089, 0.6793, 0.7468, 0.7340, 0.7457, 0.7560, 0.7432, 0.7553]  # Ajuste para 10 epochs
val_acc = [0.6667, 0.6667, 0.6500, 0.6833, 0.6333, 0.6433, 0.6500, 0.6600, 0.6700, 0.6500]

# Graficar la curva de pérdida (Loss)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(epochs, train_loss, label='Train Loss')
plt.plot(epochs, val_loss, label='Val Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Curva de Pérdida')
plt.legend()

# Graficar la curva de precisión (Accuracy)
plt.subplot(1, 2, 2)
plt.plot(epochs, train_acc, label='Train Accuracy')
plt.plot(epochs, val_acc, label='Val Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Curva de Precisión')
plt.legend()

plt.tight_layout()
plt.show()
