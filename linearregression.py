# class for Linear Regressions
class linearRegression:

  # to create this class, you need to give x and y arrays
  # so it'll deduce B0 and B1 coefficients
  def __init__(self, x, y):
    
    if (len(x) != len(y)):
      raise Exception("Arrays x and y have different lengths")

    self.x = x
    self.y = y

    sum_xy = 0
    sum_x = 0
    sum_x2 = 0
    sum_y = 0
    n = len(x)

    for i in range(0, n):
      sum_xy += x[i] * y[i]
      sum_x += x[i]
      sum_x2 += x[i] ** 2
      sum_y += y[i]

    self.x_mean = sum_x / n
    self.y_mean = sum_y / n

    self.B1 = (sum_xy - ( (sum_y * sum_x) / n) ) / (sum_x2 - (sum_x ** 2) / n)
    self.B0 = (self.y_mean) - (self.B1 * self.x_mean)
    self.R2 = self.R2()
  
  # predict a value of y with a x given based on linear regression
  def predict(self, x_value):
    if ( (type(x_value) is not int) and (type(x_value) is not float) ):
      raise Exception("A numeric value must be given")
    return (self.B0 + self.B1 * x_value)

  # return an array of y predicted values with all x given based on linear regression
  def predictAll(self):
    allPredicts = []
    for each in self.x:
      allPredicts.append( self.predict(each) )
    return allPredicts

  def R2(self):
    y_ = self.predictAll()
    SQe = 0
    Syy = 0
    for i in range(0, len(self.y)):
      SQe += (self.y[i] - y_[i]) ** 2
      Syy += (self.y[i] - self.y_mean) ** 2
    
    return (1 - SQe/Syy)

  # compare the original values to predicted values i
  def compare(self):
    import matplotlib.pyplot as plt

    plt.plot(self.x, self.y, 'g-', self.x, self.predictAll(), 'r-')
    plt.legend(['Base', 'Predict'])
    plt.title("Linear Regression")

# EXAMPLE
x = range(0, 16)
y = [1,3,5,7,9,10,9,5,6,4,7,9,6,7,11,15]
obj = linearRegression(x, y)
obj.compare()
print(obj.R2)
