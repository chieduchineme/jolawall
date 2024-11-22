# trainNN.py
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from .featureList import feature_list

# Define function to process data
def preprocess_data(X):
    # Assuming `X` is a list of such entries
    X_parsed = []
    for raw_entry in X:
        # Convert the list entry into a dictionary
        entry = dict(zip(feature_list, raw_entry))
        X_parsed.append(entry)

    structured_X = []
    for entry in X_parsed:
        description = (
            f"{entry['method']} request from {entry['source']} to {entry['original_url']} "
            f"at {entry['timestamp']} with user agent '{entry['user_agent']}' "
            f"and ASN {entry['asn']}. The request included query parameters: {entry.get('query', 'None')}, "
            f"body payload: {entry.get('body', 'None')}, headers: {entry['headers']}, cookies: {entry.get('cookies', 'None')}, "
            f"and was {'not blacklisted' if entry.get('blacklist', False) else 'blacklisted'}."
        )
        structured_X.append(description) 

    # Tokenize the text data
    tokenizer = Tokenizer(num_words=10000)

    tokenizer.fit_on_texts(structured_X)  # Fit tokenizer on all text data

    # Convert text data to sequences of integers (tokens)
    X_tokenized = tokenizer.texts_to_sequences(structured_X)  # Convert to sequences of integers

    # Pad sequences to ensure they all have the same length (500 in this case)
    X_padded = pad_sequences(X_tokenized, padding='post', maxlen=500)  # Using length 500
    return X_padded


# Define the training function
def train_model(model, X, y, epochs=3, batch_size=64):
    # Preprocess the data
    X_padded = preprocess_data(X)    
    # Convert numpy array for compatibility with TensorFlow
    X_padded = np.array(X_padded)
    # Ensure labels are binary for binary classification
    y = np.array(y).astype(float)

    # Train the model with overridden accuracies
    model.fit(
        X_padded,
        y,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.4,
        verbose=0
    )
  
    return model, X_padded