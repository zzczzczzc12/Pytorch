import torch

x = torch.Tensor([1, 2, 3, 4, 5, 6]).view(2, 3)
y_0 = torch.mean(x, dim=0)
y_1 = torch.mean(x, dim=1)
print(x)
print(y_0)
print(y_1)
#tensor([[1., 2., 3.],
#       [4., 5., 6.]])
#tensor([2.5000, 3.5000, 4.5000])
#tensor([2., 5.])
