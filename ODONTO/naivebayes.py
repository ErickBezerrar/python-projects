def accuracy(matriz_confusao):
    vp = matriz_confusao[0][0]  
    vn = matriz_confusao[1][1]  
    fn = matriz_confusao[1][0]  
    fp = matriz_confusao[0][1]  
    
    acc = ((vp + vn) / (vp + fp + fn + vn)) * 100
    return acc

def precision(matriz_confusao):
    vp = matriz_confusao[0][0]  
    fp = matriz_confusao[0][1]  
    
    prec = vp / (vp + fp)
    return prec

def recall(matriz_confusao):
    vp = matriz_confusao[0][0]  
    fn = matriz_confusao[1][0]  
    
    rec = vp / (vp + fn)
    return rec

def f1_score(matriz_confusao):
    prec = precision(matriz_confusao)
    rec = recall(matriz_confusao)
    
    f1 = (2 * prec * rec) / (prec + rec)
    return f1

matriz = [
    [383, 86],
    [45, 102]
]

print("Accuracy:", accuracy(matriz))
print("Precisionn:", precision(matriz))
print("Recall:", recall(matriz))
print("F1-score:", f1_score(matriz))
