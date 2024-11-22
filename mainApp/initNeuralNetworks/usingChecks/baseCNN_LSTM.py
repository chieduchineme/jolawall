# baseCNN_LSTM.py

from keras.optimizers import Adam, AdamW, SGD, RMSprop, Nadam, Adagrad
from keras.models import Sequential
from keras.layers import Dense
from keras.models import Sequential
from keras.regularizers import l2
from keras.layers import Embedding, Conv1D, LSTM, Dense, MaxPooling1D, Dropout, BatchNormalization, GlobalMaxPooling1D, Reshape
from keras.layers import LSTM, Bidirectional, Dense, Dropout, Reshape, LeakyReLU

# Define model (adapting your create_model function)
# def create_model(num_classes, input_length=500):
#     model = Sequential()
    
#     # Embedding Layer with L2 Regularization
#     model.add(Embedding(input_dim=10000, 
#                         output_dim=500, 
#                         input_length=input_length, 
#                         embeddings_regularizer=l2(0.01)))  # L2 regularization on embeddings
    
#     # Convolutional Layers
#     model.add(Conv1D(filters=128, kernel_size=5, activation='relu'))
#     model.add(BatchNormalization())
#     model.add(Conv1D(filters=128, kernel_size=3, activation='relu'))
#     model.add(BatchNormalization())
#     model.add(GlobalMaxPooling1D())
    
#     # Reshape to 3D (batch_size, timesteps=1, features)
#     model.add(Reshape((1, 128)))  # Adjust feature size based on Conv1D output
    
#     # Bidirectional LSTM Layer
#     model.add(Bidirectional(LSTM(128, dropout=0.3, recurrent_dropout=0.3)))
    
#     # Fully Connected Layers with L2 Regularization
#     model.add(Dense(128,kernel_regularizer=l2(0.01)))
#     model.add(LeakyReLU(alpha=0.01))  # Use LeakyReLU instead of ReLU
#     model.add(Dropout(0.4))  # Dropout for regularization
#     model.add(Dense(64,  kernel_regularizer=l2(0.01)))
#     model.add(LeakyReLU(alpha=0.01))  # Use LeakyReLU instead of ReLU
#     model.add(Dropout(0.4))  # Dropout for regularization
    
#     # Output Layer
#     model.add(Dense(num_classes, activation='softmax'))
    
#     # Optimizer with Gradient Clipping
#     optimizer = Adam(learning_rate=0.005, clipvalue=1.0) 
#     # optimizer = Adam(learning_rate=0.0005, clipvalue=1.0) 
#     # optimizer = AdamW(learning_rate=0.001, weight_decay=1e-5)
#     # optimizer = SGD(learning_rate=0.0001, momentum=0.9, nesterov=True)
#     # optimizer = RMSprop(learning_rate=0.001, rho=0.9)
#     # optimizer = Nadam(learning_rate=0.001)
#     # optimizer = Adagrad(learning_rate=0.01)


#     # Compile the Model
#     model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    
#     return model

def create_model(num_classes, input_length=500):
    model = Sequential()

    # Embedding Layer with L2 Regularization
    model.add(Embedding(
        input_dim=10000, 
        output_dim=500, 
        input_length=input_length, 
        embeddings_regularizer=l2(0.01)
    ))  # L2 regularization on embeddings

    # Convolutional Layers
    model.add(Conv1D(
        filters=128, 
        kernel_size=5, 
        activation='relu',
        kernel_initializer='glorot_uniform'
    ))
    model.add(BatchNormalization())
    model.add(Conv1D(
        filters=128, 
        kernel_size=3, 
        activation='relu',
        kernel_initializer='glorot_uniform'
    ))
    model.add(BatchNormalization())
    model.add(GlobalMaxPooling1D())

    # Reshape to 3D (batch_size, timesteps=1, features)
    model.add(Reshape((1, 128)))

    # Bidirectional LSTM Layer
    model.add(Bidirectional(
        LSTM(128, 
             dropout=0.3, 
             recurrent_dropout=0.3, 
             return_sequences=False)
    ))

    # Fully Connected Layers with L2 Regularization
    model.add(Dense(
        128, 
        kernel_regularizer=l2(0.01),
        activation='linear'
    ))
    model.add(LeakyReLU(alpha=0.01))  # LeakyReLU for better gradient flow
    model.add(Dropout(0.4))

    model.add(Dense(
        64, 
        kernel_regularizer=l2(0.01),
        activation='linear'
    ))
    model.add(LeakyReLU(alpha=0.01))  # LeakyReLU for better gradient flow
    model.add(Dropout(0.4))

    # Output Layer
    model.add(Dense(num_classes, activation='softmax'))

    # Optimizer with Gradient Clipping
    optimizer = Adam(learning_rate=5e-06, clipvalue=1.0)
    model.compile(
        loss='categorical_crossentropy', 
        optimizer=optimizer, 
        metrics=['accuracy']
    )

    return model
