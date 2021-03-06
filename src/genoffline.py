#!/usr/bin/python3.5

import sys

from model import resparser
from model import tgffparser
from ui import figure
from algo import trim

if len(sys.argv) < 2:
    print("Too few arguments!")
    exit(0)

tgff_parser = tgffparser.TgffParser()
tgff_parser.do(sys.argv[1] + ".tgff")
tgff = tgff_parser.generate_graphs()

res_parser = resparser.ResParser(tgff)
res_parser.do(sys.argv[1] + ".res")

fig = figure.Figure(tgff)
fig.offline(sys.argv[1] + ".svg")

# trim.trim_time_slack(tgff)

fig = figure.Figure(tgff)
fig.runtime(sys.argv[1] + "_rt.svg")
