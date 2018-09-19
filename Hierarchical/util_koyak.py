import pandas as pd
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def col_selector(list_feature, df_genre):
    selected_feature = []
    for feature in list_feature:
        for column in df_genre.columns:
            if feature in column:
                selected_feature.append(column)
    selected_feature.append('genre_top')
    return df_genre[selected_feature]

def grid_estimator(estimator, param_grid, X_train, y_train, X_test, y_test, cv=5, n_jobs=1):
    grid = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=cv, n_jobs=n_jobs)
    grid.fit(X_train, y_train)
    print("Accuracy training: " + str(grid.best_score_))
    y_pred = grid.predict(X_test)
    print("Accuracy test: " + str(accuracy_score(y_pred,y_test)))
    print(grid.best_estimator_)

def col_selector_hiera(list_feature, df_genre):
    selected_feature = []
    for feature in list_feature:
        for column in df_genre.columns:
            if feature in column:
                selected_feature.append(column)
    selected_feature.append('genre_selected')
    return df_genre[selected_feature]

def find_element_dictio(class_hierarchy, element):
    listOfItems = class_hierarchy.items()
    for item  in listOfItems:
        listOfKeys = []
        if element in item[1]:
            return item[0]
        else: 
            return 0


