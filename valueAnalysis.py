#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:59:49 2020

@author: chenwu
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker
#****************************
# -- please change date range and values for the count of 
#'Collaboration', 'Excellence', 'Creativity', 'Confidence', 'None'
#******************************
date = '10th-16th Jan'
height = [23, 4, 10, 9, 10]

# arrange plot size and colours
bars = ['Collaboration', 'Excellence', 'Creativity', 'Confidence', 'None']
y_pos = np.arange(len(bars))
fig, ax = plt.subplots(1, 1)
ax.grid(zorder=0)
ax.bar(y_pos, height,width=0.5,align='center', color=['skyblue', 'yellow', 'pink', 'green', 'orange'])

# value labels 
plt.xticks([])
xbox1 = TextArea("Collaboration", textprops=dict(color="darkblue", size=11))
xbox2 = TextArea("Excellence",     textprops=dict(color="#ffbf00", size=11))
xbox3 = TextArea("Creativity", textprops=dict(color="#ff00ff", size=11))
xbox4 = TextArea("Confidence",     textprops=dict(color="green", size=11))
xbox5 = TextArea("    None", textprops=dict(color="#ff8000", size=11))

xbox = HPacker(children=[xbox1, xbox2, xbox3,xbox4,xbox5],align="center", pad=0, sep=5)

anchored_xbox = AnchoredOffsetbox(loc=3, child=xbox, pad=0., frameon=False, bbox_to_anchor=(0.01, 0.5), 
                                  bbox_transform=ax.transAxes, borderpad=0.)

anchored_xbox = AnchoredOffsetbox(loc=3, child=xbox, pad=0., frameon=False, bbox_to_anchor=(0.01, -0.08), 
                                  bbox_transform=ax.transAxes, borderpad=0.)


ax.add_artist(anchored_xbox)

#graph labels

plt.xlabel('Values')
ax.xaxis.set_label_coords(0.5, -.125)
plt.ylabel('Count')
plt.title('Engineer Values '+date+' 2020')

#also can save to a file
plt.savefig(date+' values.png')
plt.show()


