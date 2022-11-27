def find_corr_x_y(x,y):
    nx = len(x)
    ny = len(y)
    if nx == ny:
        # Find the sum of the products
        prod = []
        for xi,yi in zip(x,y):
            prod.append(xi*yi)
        sum_prod_x_y = sum(prod)
        sum_x = sum(x)
        sum_y = sum(y)
        squared_sum_x = sum_x**2
        squared_sum_y = sum_y**2
        x_square = []
        for xi in x:
            x_square.append(xi**2)
        # Find the sum
        x_square_sum = sum(x_square)
        y_square=[]
        for yi in y:
            y_square.append(yi**2)
        # Find the sum
        y_square_sum = sum(y_square)

        # Use formula to calculate correlation
        numerator = nx*sum_prod_x_y - sum_x*sum_y
        denominator_term1 = nx*x_square_sum - squared_sum_x
        denominator_term2 = nx*y_square_sum - squared_sum_y
        denominator = (denominator_term1*denominator_term2)**0.5
        correlation = numerator/denominator
        return correlation
    else:
        return "The correlation coefficient can't be found."

if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    print(find_corr_x_y(x,y))