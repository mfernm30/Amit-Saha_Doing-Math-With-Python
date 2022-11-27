from pylab import plot, show, title, xlabel, ylabel, legend

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    ratios = []
    for i in range(n):
        c = a + b
        series.append(c)
        ratios.append(a/b)
        a = b
        b = c
        
    return ratios

if __name__ == '__main__':

    ratios = fibo(100) 
    numbers = range(0, 100)   
    
    plot(numbers, ratios)
    title('Fibonacci Golden Ratio')
    xlabel('Number')
    ylabel('Ratio')   
    show()


    