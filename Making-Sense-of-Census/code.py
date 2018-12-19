# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path,delimiter=",",skip_header=1)
census = np.concatenate([new_record,data])


# --------------
#Code starts here
age = census[:,0]
print(age)
max_age = age.max()
print(max_age)
min_age = age.min()
print(min_age)
age_mean = age.mean()
print(age_mean)
age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

length = np.array((len_0,len_1,len_2,len_3,len_4))
min_len = length.min()
print(min_len)
which = np.where(length == 6)
print(which)
minority_race = 3


# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = (working_hours_sum/senior_citizens_len)
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()
print(avg_pay_high)
print(avg_pay_low)


