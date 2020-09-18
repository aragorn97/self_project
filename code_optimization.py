#importing the libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("Vendor_data.csv")
data.describe()
# Initializing the increment vector - all zeros
increment = np.zeros([250])

flag = 0
increment_i = increment
#flag = 1 is the condition when the increment vector will remain the same
while (flag == 0):
    print(find_rev(increment_i))
    increment_iplus1 = incremental_new(increment_i)
    if (min(increment_iplus1 == increment_i) == 1):
        flag = 1
    increment_i = increment_iplus1
increment_i
find_rev(increment_i)
find_rev(increment)
price = increment_i
data['new_price'] = price

#This function tries to get the next best increment vector
def incremental_new(initial_increments):
    initial_rev = find_rev(initial_increments)
    intermediate_rev = 0
    for i in range(250):
        increments = initial_increments
        if increments[i] > -0.099:
            increments[i] = increments[i] - 0.01
        rev = find_rev(increments)
        if rev > initial_rev:
            final_increments = increments
        intermediate_rev = rev
        if increments[i] < 0.19: 
            increments[i] = initial_increments[i] + 0.01
        rev = find_rev(increments)
        if rev > max(initial_rev,intermediate_rev):
            final_increments = increments
    return(final_increments)

# This function will get us the overall revenue for the given increment vector
def find_rev(increment):
    price = data['Avg_Price_per_unit']*(1+increment)
    volumes = data['Average_units_sold']*(1-(data['Increase_sale_volume']*increment*10))
    multiplier = (1-(data['Incremental_acquisition']*increment*10))
    total_multiplier = 1
    for k in range(250):
        total_multiplier = total_multiplier * multiplier[k]
    profit_wo_multiplier = 0.05*(sum(price*volumes) - sum(volumes*data['Cost_per_unit']))
    profit_w_multiplier = profit_wo_multiplier*total_multiplier
    net_profit = sum(profit_w_multiplier)
    return(net_profit)


