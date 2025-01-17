import torch
from torch import nn
class Model(nn.Module):
    def __init__(self, dino, num_classes):
        super(Model, self).__init__()
        self.transformer = dino
        self.classifier = nn.Sequential(nn.Linear(1024, 256), nn.ReLU(), nn.Linear(256, num_classes))

    def forward(self, x):
        x = self.transformer(x)
        x = self.transformer.norm(x)
        x = self.classifier(x)
        return x


def init_model(classes):
    model = torch.hub.load('facebookresearch/dinov2', 'dinov2_vitl14')

    model = Model(model, classes)
    return model

def load_model(classes, filename):
    model = torch.hub.load('facebookresearch/dinov2', 'dinov2_vitl14')

    model = Model(model, classes)
    m_state_dict = torch.load(filename)
    model.load_state_dict(m_state_dict)
    return model