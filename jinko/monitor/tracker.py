import wandb
from torch.utils.tensorboard import SummaryWriter


class Tracker:

    def  __init__(self, path: str, use_wandb: bool, wandb_peoject_name: str = None):
        self.use_wandb = use_wandb
        self.path = path
        if self.use_wandb:
            assert wandb_peoject_name != None
            wandb.init(
                project=wandb_peoject_name,
                sync_tensorboard=True,
            )
        self.writer = SummaryWriter(path)

    def log(self, key, value, step):
        self.writer.add_scalar(key, value, step)
        return

    def add_config(self, config):
        if self.use_wandb:
            wandb.config = config
        return

    def close(self):
        self.writer.close()
        wandb.finish()
