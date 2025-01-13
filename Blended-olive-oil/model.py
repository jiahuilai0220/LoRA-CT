
import torch.nn as nn
class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()
        self.Conv1d_1=nn.Conv1d(in_channels=1, out_channels=16, kernel_size=5, stride=2)
        self.BatchNorm1d_1=nn.BatchNorm1d(16)
        self.RELU_1=nn.LeakyReLU()
        self.Conv1d_2=nn.Conv1d(in_channels=16, out_channels=32, kernel_size=3, stride=3)
        self.BatchNorm1d_2=nn.BatchNorm1d(32)
        self.RELU_2=nn.LeakyReLU()
        self.Conv1d_3=nn.Conv1d(in_channels=32, out_channels=64, kernel_size=5, stride=1)
        self.BatchNorm1d_3=nn.BatchNorm1d(64)
        self.RELU_3=nn.LeakyReLU()
        self.AdaptiveMaxPool1d=nn.AdaptiveMaxPool1d(100) #参数表示输出的特征维度
        self.Flatten=nn.Flatten()
        self.Linear=nn.Linear(64*100,32*100)
        self.Linear2=nn.Linear(32*100,1)
    def forward(self,input):
        output=self.Conv1d_1(input)
        output=self.BatchNorm1d_1(output)
        output=self.RELU_1(output)
        output=self.Conv1d_2(output)
        output=self.BatchNorm1d_2(output)
        output=self.RELU_2(output)
        output=self.Conv1d_3(output)
        output=self.BatchNorm1d_3(output)
        output=self.RELU_3(output)
        output=self.AdaptiveMaxPool1d(output)
        output=self.Flatten(output)
        output=self.Linear(output)
        output=self.Linear2(output)
        return output.squeeze(dim=1)