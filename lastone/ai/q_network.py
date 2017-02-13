import chainer
import chainer.functions as F
import numpy as np

class QNetwork(chainer.Chain):
    def __init__(self):
        super(QNetwork, self).__init__(
            conv1=F.Convolution2D(2, 32, ksize=3, stride=1, pad=1),
            linear1=F.Linear(None, 512),
            linear2=F.Linear(512, 256),
            linear3=F.Linear(256, 75))

    def __call__(self, state):
        h1 = self.conv1(state)
        h2 = F.relu(h1)
        h3 = self.linear1(h2)
        h4 = F.relu(h3)
        h5 = self.linear2(h4)
        h6 = F.relu(h5)
        h7 = self.linear3(h6)
        return h7
