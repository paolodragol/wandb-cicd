import wandb

print(f'The version of wandb is: {wandb.__version__}')
assert wandb.__version__ == '0.18.1', f'Expected 0.18.1, but got {wandb.__version__}'
