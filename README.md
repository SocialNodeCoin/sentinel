# AllGamesCoin Sentinel

An all-powerful toolset for AllGamesCoin.

Sentinel is an autonomous agent for persisting, processing and automating AllGamesCoin governance objects and tasks, and for expanded functions in the upcoming AllGamesCoin V0.2.x release (Evolution).

Sentinel is implemented as a Python application that binds to a local version 0.2.x allgamescoind instance on each AllGamesCoin Masternode.

This guide covers installing Sentinel onto an existing Masternode in Ubuntu 14.04 / 16.04.

## 1. Installation - Linux

### 1.1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local AllGamesCoin daemon running is at least version 0.2.0 (20000)

    $ allgamescoin-cli getinfo | grep version

### 1.2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/allgamescoindev/sentinel.git && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 1.3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### 1.4. Test the Configuration

Test the config by running all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with allgamescoind and the installation is complete

## Installation - Windows

### 1.1. Install Prerequisites

Download and install Python 2.7 https://www.python.org/

Open CMD

pip install pyinstaller

### 1.2. build

Download https://github.com/allgamescoindev/sentinel.git

Go to the unzipped folder

pip install -r requirements.txt

pyinstaller --onefile --paths=lib/ ./bin/sentinel.py

## Configuration

An alternative (non-default) path to the `allgamescoin.conf` file can be specified in `sentinel.conf`:

    allgamescoin_conf=/path/to/allgamescoin.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

### License

Released under the MIT license, under the same terms as AllGamesCoinCore itself. See [LICENSE](LICENSE) for more info.
