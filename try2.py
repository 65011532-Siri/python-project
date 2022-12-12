food = 0
trans = 1
enter = 0
sport = 1
invest = 0
other = 1
expense_sum = [food,trans,enter,sport,invest,other]
expense_cate = ["Food and Beverage", "Transportatino and gas", "Entertainment","Sport","Investment","Others Expenses"]
exp = [0.1,0,0.1,0.1,0.1,0]
if food == 0:
    expense_sum.remove(food)
    expense_cate.remove("Food and Beverage")
    exp.remove(0.1)
print(expense_sum)
print(expense_cate)
print(exp)