"""
Aim is to calculate Coefficient of Determination-R2 score
Formula is R2= 1- SSres / SStot
SSres is the sum of squares of the residual errors.
SStot is the total sum of the errors.
SSres = sum((actual-predicted)**2)
SStot = sum((actual-mean)**2)
We are implementing results using two methods
Method 1: Everything is implemented from scratch
Method 2: Using sklearn metrics method r2_score
Method 3: Class based approach
"""
from sklearn.metrics import r2_score

# Method 1
print("====================METHOD 1============================")
def list_sum(list_actual):
	total = 0
	for i in range(len(list_actual)):
		total = total + list_actual[i]
	return total

y_actual = [1, 1.2, 1.3]
y_predicted = [0.9, 1.4, 1.2]
sum_y_actual = list_sum(y_actual)
mean_y_actual = sum_y_actual/len(y_actual)

square_difference_ssr=list()
zip_object = zip(y_actual, y_predicted)
for list1_i, list2_i in zip_object:
    square_difference_ssr.append((list1_i-list2_i)**2)

ssr = sum(square_difference_ssr)
print("SSR is", ssr)
print('-'*40)
square_difference_sst = [(each - mean_y_actual)**2 for each in y_actual]
sst = sum(square_difference_sst)
print("SST is", sst)
print('-'*40)
R_squared = 1-(ssr/sst)
print("Coefficient of determination [1- ssr/sst] is", R_squared)
# Method 2
print("====================METHOD 2============================")
R_squared = r2_score(y_actual, y_predicted)
print("Output using method of sklearn r2_score is: {}".format(R_squared))
# Method 3: Class Based approach
print("====================METHOD 3============================")

class Rsquared:

	def __init__(self, y_actual_list, y_predicted_list):
		self.y_actual_list = y_actual_list
		self.y_predicted_list = y_predicted_list

	def display_list(self):
		print("Actual list passed as :", self.y_actual_list)
		print("Predicted list passed as:", self.y_predicted_list)

	def calculating_rsquare(self):
		sum_y_actual = list_sum(self.y_actual_list)
		mean_y_actual = sum_y_actual/len(self.y_actual_list)
		square_difference_ssr=list()
		zip_object = zip(self.y_actual_list, self.y_predicted_list)
		
		for list1_i, list2_i in zip_object:
			square_difference_ssr.append((list1_i-list2_i)**2)
		ssr = sum(square_difference_ssr)
		square_difference_sst = [(each - mean_y_actual)**2 for each in self.y_actual_list]
		sst = sum(square_difference_sst)
		R_squared = 1-(ssr/sst)
		return R_squared

#object_rsquared = R_squared()		
object_rsquared = Rsquared(y_actual, y_predicted)
object_rsquared.display_list()
R_squared_class = object_rsquared.calculating_rsquare()
print("Output using class method is: {}".format(R_squared_class))
"""
There is another concept so called adjusted squaredR which is very important to know. Squared R will increase or change when one adds new variable to the regression \
equation irrespective of whether such variable is important or not. But adjusted squaredR will only change if the added new variable or regressor is significant.
Formulae to calculate adjusted squaredR  is as below:-
adjusted_R_square = 1-[(1-R_squared)(n-1)/n-k-1]
where n: number of samples or number of observations
      k: numbers of independent variables or numbers of regressors
      R_squared : Rsquared
"""      
