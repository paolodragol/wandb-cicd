import wandb

print(f'The version of wandb is: {wandb.__version__}')
assert wandb.__version__ == '2.1.01', f'Expected 2.01.11, but got {wandb.__version__}'