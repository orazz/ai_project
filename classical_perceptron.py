import cmath
import numpy as np
from decimal import getcontext, Decimal

# Set the precision.
getcontext().prec = 4

def predict(inputs,weights):
    activation=(0.0)
    res = ''
    for i,w in zip(inputs,weights):
        activation += (i)*(w)
        res += ("%0.4f * %0.4f + "%(i,w))
    print("net = ",(res[:-3]),"= %0.4f"%(activation))
    return (1.0 if activation>=0.0 else 0.0, activation)

def calc_delta_weight(d_error, inputs, row):
    delta_w = np.zeros(row)
    oneline = ""
    for i, inp in enumerate(inputs):
        delta_w[i] = (d_error) * (inp)
        oneline += f"Δw{(0 if i == len(inputs)-1 else i+1)} = {delta_w[i]}  "
    print(f"{oneline[:-2]}\n")
    return delta_w

def accuracy(matrix,weights,coefficient):
    num_errors = 0.0
    d_arr = np.zeros(len(matrix))
    delta_weights = np.zeros((len(matrix),len(matrix)))
    for i in range(len(matrix)):
        print(f"Training example {i+1}")
        (pred, activation) = predict(matrix[i][:-1],weights)

        d_arr[i] = matrix[i][-1]-pred
        print(f"Δ = Os - Oc = {matrix[i][-1]} - {pred} = {d_arr[i]}")
        
        delta_weights[i] += calc_delta_weight(d_arr[i], matrix[i][:-1], len(matrix))
        oneline_weights = ""
        for j in range(len(weights)):
                oneline_weights += "%0.4f, " %(weights[j])
    return (weights, d_arr, delta_weights)
        
def calc(matrix, weights, coefficient, epoch):
    oneline_weights = ""
    oneline = ""
    d_sum = 0.0
    print(f"\n\t\t\tTraining epoch {epoch}\n")
    (new_weights, d_arr, delta_weights) = accuracy(matrix,weights,coefficient)
    
    for d in d_arr:
        d_sum += cmath.sqrt(d)
        oneline += f"{d}^2 + "
    print(f"Calculate total error from epoch {epoch}")
    print(f"E = ΣE^2 = {oneline[:-2]}= {abs(d_sum)} {'>=' if abs(d_sum) >= coefficient else '<'} {coefficient}")

    delta_weights_sum = np.zeros(len(matrix))
    for dw in delta_weights:
        for i, dwe in enumerate(dw):
            delta_weights_sum[i] += dwe   

    for i, nw in enumerate(weights):
        weights[i] = nw + delta_weights_sum[i] 
        print("w%0.0f = %0.4f + %0.4f = %0.4f" %(0 if i == len(weights)-1 else i+1, nw, delta_weights_sum[i], weights[i]))

    if d_sum == 0:
        print(f"\nResult:")
        for j in range(len(new_weights)):
            # sys.stdout.write("\tWeight[%d]: %0.2f \n"%(j,new_weights[j]))
            oneline_weights += "%0.2f, " %(new_weights[j])
        print(f"weights: {oneline_weights[:-2]}\n")
        return True
    else:
        return False

def main():
    static = True

    static = bool(int(input("Static data: ")))
    epoch = 1

    if (static):
        matrix = [    
                    [0.3,     0.3,    0.2,  1.0,  1.0],
                    [0.4,    -0.3,   -0.1,  1.0,  1.0],
                    [-0.2,   -0.1,    0.2,  1.0,  0.0],
                    [0.0,     0.1,    0.0,  1.0,  0.0]
                ]
        
        weights = [0.25, 0.15, -0.30, -0.5]
        coefficient = 0.02

        # matrix = [    
        #             [-0.4,   -0.4,    1.0,  1.0],
        #             [-0.4,    0.4,    1.0,  1.0],
        #             [0.3,    -0.4,    1.0,  0.0],
        #             [0.0,     1.0,    1.0,  0.0]
        #         ]
        
        # weights = [-0.8221, -0.4942, 0.2123]
        # coefficient = 0.01

        while (True):
            if calc(matrix, weights, coefficient, epoch):
                break
            epoch += 1
    else:
        columns = 0
        number_of_inputs = 0
        matrix = []
        coefficient = 0
        weights = []
        errors = 0
        oneline_weights = ""
        
        while(True):
            if columns != 0 and columns != '' and number_of_inputs != 0 and number_of_inputs != '' and len(matrix) >= columns and coefficient > 0 and len(weights) > number_of_inputs and errors == True:
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
                    while (True):
                        errors = calc(matrix, weights, coefficient, epoch)
                        if errors:
                            break
                        epoch += 1

if __name__ == '__main__':
    main()
