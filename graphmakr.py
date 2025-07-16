import matplotlib.pyplot as plt


#needs to be a to take a value split it into  and split it into x and y and make a plot diagram

class Graph():
    def __init__(self, x_value, y_value):
        if not x_value or not y_value:
            raise ValueError('you did not enter any values')
        
        self.x_value = x_value
        self.y_value = y_value
       
    @staticmethod
    def get_XandY():
        y_value = []
        x_value = []
        values = input('Type the cordinates like this "x,y" with space between them: ')
        pairs = values.split() # returns a list with each pair 
        for pair in pairs:
            x, y = pair.split(',')
            x_value.append(float(x))
            y_value.append(float(y))
        return x_value, y_value
    
    
    def makegrph(self):
            plt.scatter(self.x_value, self.y_value)
            plt.savefig('scatterplt.png')
            plt.show()
        
        
def main():
    xvalue, yvalue = Graph.get_XandY()
    
    graph = Graph(xvalue, yvalue)
    
    graph.makegrph() # we have already idented the values so need to type them again here
        
if __name__ == '__main__':
    main()