import numpy as PY
length_user = 3
length_capacity = 3
length_candidate =3
cost_different=[0,1,2] 
#cost_different is different cost for each user in differnet form. 
#Notice that we assume the users which has even number has double cost than others 
value_different=[0,1,2] 
#value_different is the schedling value of each user with different form
#we assume that the user with even number has trible value than others
length_cost = len(cost_different)

class Cost():
    def __init__(self,length_user,length_cost):
        self.mat_cost = PY.zeros((length_user+1,length_cost))
        self.mat_value = PY.zeros((length_user+1,length_cost))
    def define_cost(self,cost_different):
        cost_diff=PY.array(cost_different)
        for counter_user in range(length_user+1):
            if counter_user != 0:
                if (counter_user%2) ==0:
                    self.mat_cost[counter_user,:] = cost_diff*2
                    continue
                self.mat_cost[counter_user,:] = cost_diff
    def define_value(self,value_different):
        val_diff=PY.array(value_different)
        for counter_user in range(length_user+1):
            if counter_user != 0:
                if (counter_user%2) ==0:
                    self.mat_value[counter_user,:] = val_diff*3
                    continue
                self.mat_value[counter_user,:] = val_diff

class Knapsack():
    def __init__(self,length_user,length_capacity,length_candidate,Cost):
        self.mat = PY.zeros((length_user+1,length_capacity+1,length_candidate+1))
        self.solution_user = PY.zeros((length_candidate))
        self.solution_cost = PY.zeros((length_candidate))
    def recursive(self,length_user,length_capacity,length_candidate,Cost):
        for counter_candidate in range(1,length_candidate+1,1):
            for counter_user in range(1,length_user+1,1):
                for counter_capacity in range(1,length_capacity+1,1):
                    for counter_cost in range(0,length_cost,1):
                        temp =0
                        if (counter_capacity-Cost.mat_cost[counter_user,counter_cost] >=0):
                            temp = Cost.mat_value[counter_user,counter_cost] +self.mat[counter_user-1,counter_capacity-counter_cost,counter_candidate-1]
                        if(self.mat[counter_user,counter_capacity,counter_candidate] < temp):
                            self.mat[counter_user,counter_capacity,counter_candidate] = temp
        counter_candidate = length_candidate
        counter_user = length_user
        counter_capacity = length_capacity
        counter_sol =0
        while(1):
            if((counter_candidate <=0) or (counter_user <=0) or (counter_capacity <=0)):
                break
            for counter_cost in range(1,length_cost,1):
                temp = int(counter_capacity-Cost.mat_cost[counter_user-1,counter_cost])
                if(self.mat[counter_user-1,counter_capacity,counter_candidate] ==self.mat[counter_user,counter_capacity,counter_candidate]):
                    counter_user = counter_user -1
                    break
                else:
                    if(self.mat[counter_user,counter_capacity,counter_candidate] ==self.mat[counter_user-1,temp,counter_candidate-1]+ Cost.mat_value[counter_user,counter_cost]):
                        self.solution_user[counter_sol] = counter_user
                        self.solution_cost[counter_sol] = counter_cost
                        counter_sol= counter_sol +1
                        counter_user =counter_user-1
                        counter_capacity = int(counter_capacity - Cost.mat_cost[counter_user-1,counter_cost])
                        counter_candidate =counter_candidate -1
                        break
                if(counter_candidate <=0 or counter_user <= 0 or counter_capacity <= 0):
                    break
Cost = Cost(length_user,length_cost)
Cost.define_cost(cost_different)
Cost.define_value(value_different)
Knapsack = Knapsack(length_user,length_capacity,length_candidate,Cost)
Knapsack.recursive(length_user,length_capacity,length_candidate,Cost)
print('Knapsack->{0}'.format(Knapsack.mat))
print('Cost->{0}'.format(Cost.mat_cost))
print('Value->{0}'.format(Cost.mat_value))
print('user->{0}'.format(Knapsack.solution_user))
print('form->{0}'.format(Knapsack.solution_cost))
