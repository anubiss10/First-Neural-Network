
import tensorflow as tf
import numpy as np

celsius = np.array([-40,-10,0,8,15,22,48], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)

#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo = tf.keras.Sequential([capa])

oculta1= tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2= tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1,oculta2,salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado")

import matplotlib.pyplot as plt
plt.xlabel(" # Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])

print('Realizando una prediccion.')
input_data = np.array([[100.0]])
resultado = modelo.predict(input_data)
print('El resultado es: '+ str(resultado) + ' fahrenheit')

print("Variables internas del modelo")
#print(capa.get_weights())
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())