matrix = [[383, 86],
          [45, 102]]


vp = matrix[0][0]
vn = matrix[1][1]
fn = matrix[1][0]
fp = matrix[0][1]


def accuracy(matrix):

    vp = matrix[0][0]
    vn = matrix[1][1]
    fn = matrix[1][0]
    fp = matrix[0][1]  
    return ((vp + vn)/(vp + fp + fn + vn)) * 100
print("função accuracy: ", accuracy(matrix))


def precision(matrix):
    return vp/(vp + fp) 
print("função precision: ", precision())

def recall():
    return vp/(vp + fn)
print("função recall: ", recall())


def f1_score():
    return (2 * precision() * recall())/(precision() + recall())
print("função f1-score: ", f1_score())