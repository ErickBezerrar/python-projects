def accuracy(conf_matrix):
    vp = conf_matrix[0][0]
    vn = conf_matrix[1][1]
    fn = conf_matrix[1][0]
    fp = conf_matrix[0][1]
    
    acc = ((vp + vn) / (vp + fp + fn + vn)) * 100
    return acc

def precision(conf_matrix):
    vp = conf_matrix[0][0]
    fp = conf_matrix[0][1]
    
    prec = vp / (vp + fp)
    return prec

def recall(conf_matrix):
    vp = conf_matrix[0][0]
    fn = conf_matrix[1][0]
    
    rec = vp / (vp + fn)
    return rec

def f1_score(conf_matrix):
    prec = precision(conf_matrix)
    rec = recall(conf_matrix)
    
    f1 = (2 * prec * rec) / (prec + rec)
    return f1

confusion_matrix_J48 = [
    [455, 14],
    [50, 97]
]

print("Accuracy:", accuracy(confusion_matrix_J48))
print("Precision:", precision(confusion_matrix_J48))
print("Recall:", recall(confusion_matrix_J48))
print("F1-score:", f1_score(confusion_matrix_J48))
