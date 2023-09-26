import torch
import os
from torch import nn
from icecream import ic


class Net(nn.Module):
    def __init__(self, type='BN', c=32, H=256, W=256) -> None:
        super().__init__()

        if type == 'BN':
            # BN
            self.bn = nn.BatchNorm2d(c)
            """
            ic| model: Net(
                (bn): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            )
            ic| model_state_dict['bn.weight'].shape: torch.Size([32])
            ic| model_state_dict['bn.bias'].shape: torch.Size([32])
            """

        elif type == 'LN':
            self.ln = nn.LayerNorm([c, H, W])
            """
            ic| model: Net(
                (ln): LayerNorm((32, 256, 256), eps=1e-05, elementwise_affine=True)
            )
            ln.weight
            ln.bias
            ic| model_state_dict['ln.weight'].shape: torch.Size([32, 256, 256])
            ic| model_state_dict['ln.bias'].shape: torch.Size([32, 256, 256])
            """
            
        elif type == 'IN':
            self.instance_norm = nn.InstanceNorm2d(c)
            
        elif type == 'GN':
            self.gn = nn.GroupNorm(num_groups=8, num_channels=c)
            
        else:
            pass

        # self.gn = nn.GroupNorm()

    def forward(self, x):
        if type == 'BN':
            x = self.bn(x)
            
        elif type == 'LN':
            x = self.ln(x)
            
        elif type == 'IN':
            x = self.instance_norm(x)
            
        elif type == 'GN':
            x = self.gn(x)
            
        return x


def test_net(type='BN'):
    ic(type)
    
    model = Net(type)

    img = torch.randn((12, 32, 256, 256))
    print(img.shape)

    out = model(img)

    print(out.shape)

    model_state_dict = model.state_dict()

    ic(model)
    # ic(model_state_dict.items())

    for k, v in model_state_dict.items():
        ic(k, v.shape)


def main():
    test_net('BN')

    print('\n'*3)
    
    test_net('LN')
    
    print('\n'*3)
    
    test_net('IN')
    
    print('\n'*3)
    
    test_net('GN')

    out = 1


if __name__ == '__main__':
    main()
