import numpy as np
import matplotlib.pyplot as plt

#Example Arrays to copy and Paste
#X = -5,-2, 0, 4, 5, 6, 7
#y = 25, 4, 0, 16, 25, 36, 49


class Regression:

    def __init__(self, x, y):
        self.array1 = x
        self.array2 = y
    def __scatterData__(self, ttl):
        self.title = ttl

        plt.subplot(2,2,1)
        plt.scatter(self.array1, self.array2, color='pink', label="Data Points")
        plt.xlabel("X")
        plt.ylabel('y')
        plt.title(self.title)
        plt.show()
        plt.subplot(2,2,4)
        plt.plot(self.array1, self.array2)
        plt.xlabel('X')
        plt.ylabel('y')
        plt.title(self.title)
        plt.show()
        opt(self.array1, self.array2)

    def __regression__(self, deg ):
        self.degree= deg
        range_input = range(1, (self.degree + 1),1)
        for number in range_input:
            print(f"Model{number}:")
            print(np.poly1d(np.polyfit(self.array1, self.array2, number)))
       
    def __plot_models__(self, x_min, x_max, deg_2):
        self.min = x_min
        self.max = x_max
        self.model_number = deg_2

        x_values = np.linspace(self.min, self.max, 100)
        model = np.poly1d(np.polyfit(self.array1, self.array2, self.model_number))
        plt.plot(x_values, model(x_values), label=f"model{self.model_number}")
        plt.title(f"Chosen Regression Model{self.model_number}")
        plt.legend()
        plt.show()

        opt(self.array1, self.array2)

    def __predict__(self, modelnum, pred):
        self.prediction = pred
        model = np.poly1d(np.polyfit(self.array1, self.array2, modelnum))
        print(f"X: {self.prediction} Prediction: {model(self.prediction)}")
        opt(self.array1, self.array2)


def opt(X, y):
    print("Options:") 
    print("[1] Plot My Data")
    print("[2] Regression")
    print("[3] Predict")
    data = Regression(X, y)
    option = input("Chose an Option: ")
    if option == '1':
        title = input('insert plot title: ')
    
        return data.__scatterData__(title)
    if option == '2':
        number_of_models = int(input('Enter the # of models you want'))
        data.__regression__(number_of_models)
        
        print("Options:") 
        print("[1] Plot A model")
        choice = input("Chose an Option: ")
        if choice == '1':
            model_plt = int(input("Chose a model to plot Ex: 3: "))
            min_X = int(input("min X (linspace):"))
            max_X = int(input("max X (linspace):"))
            data.__plot_models__(max_X, min_X, model_plt)
    if option == '3':
        mod_num = int(input("wich model do you want to predict with"))
        predic = int(input("Whats your X?: "))
        data.__predict__(mod_num, predic)



def start():
    independent = list(input('Enter your Independent array no brackets Ex: 1,2,3 (X):').split(','))
    X = []

    for num in independent:
        X.append(int(num))

    dependent = list(input('Enter your Dependent array no brackets Ex: 3,2,1 (y):').split(','))
    y = []

    for numb in dependent:

        y.append(int(numb))

    if len(X) != len(y):
        print(f'Error Array X has {len(independent)} values and Array y has {len(dependent)} values try again')
        start()
    else:
        print(f'your X Array: {X} your y array: {y}')
        opt(X, y)
    

       
start()
