import numpy
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import plot_model
import numpy as np

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))


# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)



model.summary()
print(model.to_yaml())