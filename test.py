import os

os.system("pip install bscscan-python")

from bscscan import BscScan

async with BscScan("3EEZU264AG3JHV85U6JEK243925HV6BE6B") as bsc:
    print(await bsc.get_bnb_balance(address="0xBe1a088aDE3a46Ea63d47EfE7fA9B3ADc97F8DcC"))
