'''
Example of drawing a horizontal bar chart
'''
import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    # Number of bars
    num_bars = len(labels)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Expenses')
    plt.ylabel('Categories')
    plt.title('My expenses')
    # Turns on the grid which may assist in visual estimation
    plt.grid()

if __name__ == '__main__':

    categories = []
    expenses = []

    try:
        n_categories = int(input('Enter the number of categories: '))
        
        for i in range(n_categories):
            try:
                category = input('Enter category: ')
                expenditure = float(input('Expenditure: ')) 
                categories.append(category)
                expenses.append(expenditure)
            except ValueError:
                print('Invalid Expenditure.')

    except ValueError:
        print('Invalid number of categories.')
    else:
        create_bar_chart(expenses, categories)
        plt.show()