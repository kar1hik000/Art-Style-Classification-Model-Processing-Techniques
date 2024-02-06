import numpy as np

def euclidean_distance(x1, x2):
   
    return np.sqrt(np.sum((x1 - x2)**2))

def knn_predict(X_train, y_train, X_test, k):
   
    y_pred = []  
    
    for test_point in X_test:
        distances = []  

        for train_point in X_train:
            dist = euclidean_distance(test_point, train_point)
            distances.append(dist)
        
        nearest_indices = np.argsort(distances)[:k]
        
        nearest_labels = y_train[nearest_indices]
        
        pred_label = np.bincount(nearest_labels).argmax()
        y_pred.append(pred_label)
    
    return np.array(y_pred)

