import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree


# the function getting
def DecisionTree(areaCategory, Floor, Storage, publicTransport, publicParking):
    # get the csv file into df
    df = pd.read_csv('dataset.csv', encoding="ISO-8859-1")
    df.head()

    # drop the Score coll and save the rest in inputs
    # the Score coll will save in target
    inputs = df.drop('Success category', axis=1)
    target = df['Success category']

    # convert the following cols to numbers (need to do it for all our text data in the cells
    # we are not actually convert, it will generate a new cols with  the data in numbers

    le_storage = LabelEncoder()
    le_Public_Transport = LabelEncoder()
    le_Public_parking = LabelEncoder()

    inputs['storage_n'] = le_Public_Transport.fit_transform(inputs['storage'])
    inputs['Public_Transport_n'] = le_Public_Transport.fit_transform(inputs['Public Transport'])
    inputs['Public_parking_n'] = le_Public_Transport.fit_transform(inputs['Public parking'])

    # dropping the old cols
    inputs_n = inputs.drop(
        ['name', 'State', 'City', 'Type', 'lattitude', 'address', 'longitude', 'area (mÂ²)', 'storage',
         'Public Transport',
         'Public parking', 'rating', 'Number of reviews', 'Success Score '], axis=1)

    # generate decision tree model
    model = tree.DecisionTreeClassifier()

    # train the model
    model.fit(inputs_n, target)

    # not sure what the score out put mean
    # model.score(inputs_n, target)

    return model.predict([[areaCategory, Floor, Storage, publicTransport, publicParking]])
    #return model.predict([[1, 0, 0, 1, 1]])

#
# # test
# model.predict([[1, 0, 1, 0, 1]])
# # array([0])
# model.predict([[1, 1, 1, 1, 1]])
# # array([1])
# model.predict([[0, 1, 1, 1, 1]])
# # array([1])
# model.predict([[2, 0, 1, 1, 1]])
# # array([1])
# model.predict([[1, 0, 0, 0, 0]])
# # array([1])
# model.predict([[0, 0, 0, 0, 0]])
# # array([1])

 # array([2])
