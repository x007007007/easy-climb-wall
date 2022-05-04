#!/bin/bash

python -m x007007007.easy-climb-wall migrate
python -m x007007007.easy-climb-wall proxy_watchdog &

exec $@