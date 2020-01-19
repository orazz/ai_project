import numpy as np

def predict(inputs,weights):
    activation=(0.0)
    res = ''
    for i,w in zip(inputs,weights):
        activation += i*w
        res += ("%0.0f * %0.2f + "%(i,w))
    print("net = ",(res[:-3]),f"= {activation}")
    return (1.0 if activation>=0.0 else 0.0, activation)

def accuracy(matrix,weights,coefficient):
    num_errors = 0.0
    for i in range(len(matrix)):
        print(f"Training example {i+1}")
        (pred, activation) = predict(matrix[i][:-1],weights)
        if activation >= 0:
            print("that is greater than 0, so Oc = %0.0f, and Os = %0.0f"%(pred, matrix[i][-1]))
        else:
            print("that is less than 0, so Oc = %0.0f, and Os = %0.0f"%(pred, matrix[i][-1]))

        if pred!=matrix[i][-1]:
            num_errors += 1
            if pred == 1:
                for j in range(len(matrix[i])-1):                
                    if matrix[i][j] > 0:
                        weights[j] = (weights[j]) - (coefficient)
                print(f"so weights will be adjusted by decremented with d = {coefficient} on active connections")
            else:
                for j in range(len(matrix[i])-1):                
                    if matrix[i][j] > 0:
                        weights[j] = (weights[j]) + (coefficient)
                print(f"so weights will be adjusted by incremented with d = {coefficient} on active connections")

        oneline_weights = ""
        for j in range(len(weights)):
                oneline_weights += "%0.2f, " %(weights[j])
        print(f"weights: {oneline_weights[:-2]}\n")
    return (weights, num_errors)
        

def main():
    columns = 0
    number_of_inputs = 0
    matrix = []
    coefficient = 0
    weights = []
    errors = 1
    oneline_weights = ""
    
    while(True):
        if columns != 0 and columns != '' and number_of_inputs != 0 and number_of_inputs != '' and len(matrix) >= columns and coefficient > 0 and len(weights) > number_of_inputs and errors <= 0:
            break
        else:
            if columns == 0 or columns == '':
                columns = int(input("Enter the number of columns: "))
            elif number_of_inputs == 0 or number_of_inputs == '':
                number_of_inputs = int(input("Enter the number of inputs <x>: "))
            elif columns > 0 and number_of_inputs > 0 and len(matrix) < columns:
                matrix = np.zeros((columns,number_of_inputs+2))
                for x in range(columns):
                    for inp in range(0, number_of_inputs+2):
                        if inp+2 == number_of_inputs+2:
                            matrix[x][inp] = float(input(f"Ex{x+1} - x0: "))
                        elif inp+1 == number_of_inputs+2:
                            matrix[x][inp] = float(input(f"Ex{x+1} - Os: "))
                        else:
                            matrix[x][inp] = float(input(f"Ex{x+1} - x{inp+1}: "))
                    print("----")
            elif coefficient <= 0:
                coefficient = float(input("Enter the coefficient: "))
            elif len(weights) <= number_of_inputs:
                weights = np.zeros(number_of_inputs+1)
                for w in range(number_of_inputs+1):
                    if w == number_of_inputs:
                        weights[w] = float(input(f"w0: "))
                    else:
                        weights[w] = float(input(f"w{w+1}: "))
            else:
                epoch = 1
                while (True):
                    print(f"\n\t\t\tTraining epoch {epoch}\n")
                    (new_weights, errors) = accuracy(matrix,weights,coefficient)
                    weights = new_weights
                    if errors <= 0:
                        print(f"Result:")
                        for j in range(len(new_weights)):
                                oneline_weights += "%0.2f, " %(new_weights[j])
                        print(f"weights: {oneline_weights[:-2]}\n")
                        break
                    epoch += 1

if __name__ == '__main__':
    main()
