'''
Date: 2021-09-13 09:52:49
LastEditors: Liuliang
LastEditTime: 2021-09-13 10:05:01
Description: 
'''
import torch
from torch import tensor
from torch._C import ModuleDict


x = torch.rand(3,1)
# x= tensor(x,requires_grad=True)
w = torch.rand(3,3)
w= tensor(w,requires_grad=True)
# label = torch.rand(3,1)
y_lable = torch.rand(3,1)

y = w * x
z = y - y_lable

z.backward()
print(y.shape)



