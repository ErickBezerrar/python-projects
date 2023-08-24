confusion_matrix_J48 = [[455, 14],
                    [50, 97]]

vp = confusion_matrix_J48[0][0]
vn = confusion_matrix_J48[1][1]
fn = confusion_matrix_J48[1][0]
fp = confusion_matrix_J48[0][1]


def accuracy():
    return ((vp + vn)/(vp + fp + fn + vn)) * 100
print("função accuracy: ", accuracy())


def precision():
    return vp/(vp + fp) 
print("função precision: ", precision())

def recall():
    return vp/(vp + fn)
print("função recall: ", recall())


def f1_score():
    return (2 * precision() * recall())/(precision() + recall())
print("função f1-score: ", f1_score())