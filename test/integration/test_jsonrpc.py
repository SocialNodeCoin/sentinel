import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from decentralwayd import decentralwaydaemon
from decentralway_config import decentralwayConfig


def test_decentralwayd():
    config_text = decentralwayConfig.slurp_config_file(config.decentralway_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'0000043c6374e2da57aca089e7a5110f7848349c44a4522c3066ba1abf126633'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c'

    creds = decentralwayConfig.get_rpc_creds(config_text, network)
    decentralwayd = decentralwaydaemon(**creds)
    assert decentralwayd.rpc_command is not None

    assert hasattr(decentralwayd, 'rpc_connection')

    # decentralway testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    info = decentralwayd.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert decentralwayd.rpc_command('getblockhash', 0) == genesis_hash
