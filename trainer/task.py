#Read excel files

from pandas import read_excel

dataset = read_excel('gs://labtesting//irisdataset.xlsx', sheet_name = 'Sheet1')

X = dataset.iloc[:,1:-1].values             
y = dataset.iloc[:,-1:].values

print('Encoding Categorical Data')
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y.ravel())

print('Splitting the dataset into the Training set and Test set')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = None ,shuffle=True)

from sklearn.svm import SVC
classifier = SVC(C=2,gamma=0.2,kernel = 'rbf', random_state =1,max_iter=100000)
classifier.fit(X_train, y_train)

score = classifier.score(X_test,y_test)
print('Score = ',score*100)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)