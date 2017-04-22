#!/bin/bash
for x in `ps -L u n | grep "python server.py" | tr -s " " | cut -d " " -f 3`
do
  kill -9 $x
done
python server.py
