import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from scipy.spatial.distance import cdist

def decode_indices(label_encoder, sorted_indices):
    sorted_classes = []
    
    for idx in sorted_indices:
        # print("idx: ", idx)
        try:
            # Attempt to inverse transform the index
            class_label = label_encoder.inverse_transform([idx])[0]  # Only transform one index at a time
            sorted_classes.append(class_label)  # If successful, append the class
        except ValueError:
            # Handle unknown class case
            class_label = embeddingclassifier(label_encoder, idx)
            sorted_classes.append(class_label)
    return sorted_classes


def embeddingclassifier(label_encoder, unknown_label):
    # Retrieve the mapping
    label_mapping = dict(zip(range(len(label_encoder.classes_)), label_encoder.classes_))
    encoded_labels_array = np.array(list(label_mapping.keys())).reshape(-1, 1)  # Ensure this is 2D
    known_labels_array = np.array(list(label_mapping.values()))

    onehot_encoder = OneHotEncoder(sparse_output=False)  # Updated parameter
    # Fit OneHotEncoder with the encoded labels
    onehot_encoder.fit(encoded_labels_array) 

    # Normalize known data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(encoded_labels_array)  # Normalize the features
    y_train = label_encoder.fit_transform(known_labels_array)

    # Train a kNN classifier
    knn = KNeighborsClassifier(n_neighbors=1)  # Use k=1 for nearest neighbor
    knn.fit(X_train, y_train)

    unknown_label_normalized = scaler.transform(np.array([[unknown_label]]))  # Reshape to 2D for one sample
    distances = cdist(unknown_label_normalized, X_train, metric='euclidean')

    # Sort distances and get the index of the second smallest distance
    sorted_indices = np.argsort(distances[0])  # Sort distances in ascending order
    best_index = sorted_indices[1]  # Get the index of the second closest neighbor

    # Get the corresponding class of the second closest neighbor
    best_class = y_train[best_index]

    # Convert back to original label
    best_label = label_encoder.inverse_transform([best_class])
    return best_label

