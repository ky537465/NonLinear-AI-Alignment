import matplotlib.pyplot as plt
import numpy as np

# --- GLOBAL VARIABLES --- #
color1 = 'blue'
color2 = 'red'
color3 = 'green'
title = 14
info = 12
linestyle = '--'
figsize = (10,6)
barWidth = 0.35
padding = 3

set1 = '#5DADE2'
set2 = '#AED6F1'

# --- UTILITY GRAPHS --- #
x = np.linspace(0, 10, 100)

linear_util = x
increasing_util = x**2
decreasing_util = np.sqrt(x)

plt.figure(figsize=figsize)

plt.plot(x, linear_util, label="Linear Utility", color=color1, linestyle=linestyle)
plt.plot(x, increasing_util, label="Increasing Marginal Utility", color=color2, linestyle=linestyle)
plt.plot(x, decreasing_util, label="Decreasing Marginal Utility", color=color3, linestyle=linestyle)

plt.title('Types of Utility Functions', fontsize=title)
plt.xlabel("Quantity", fontsize=info)
plt.ylabel("Total Utility", fontsize=info)
plt.legend()
plt.grid(True, alpha=0.3)

#plt.show()

# --- EMOTION GRAPHS --- #
labels = ["Shame", "Gratitude", "Awe", "Confusion", "Frustration"]
before = [1.48, 3.59, 2.27, 2.0, 1.92]
after = [1.35, 3.02, 1.99, 2.48, 2.26]

x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=figsize)

rects1 = ax.bar(x - barWidth/2, before, barWidth, label='Before', color=set1)
rects2 = ax.bar(x + barWidth/2, after, barWidth, label='After', color=set2)

ax.set_ylabel('Averages', fontsize=info)
ax.set_title('Average Emotion Ratings Before & After', fontsize=title)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.bar_label(rects1, padding=padding)
ax.bar_label(rects2, padding=padding)
fig.tight_layout()
plt.show()

# -- Instructions VS Descriptions -- #
utilCats = ['Linear Utility', 'Increasing Marginal Utility', 'Decreasing Marginal Utility', 'Random Utility']
riskCats = ['Linear without Risk', 'Linear with Risk']

utilInstructions = [1280, 448, 364, 480]
utilDescriptions = [1440, 416, 564, 448]
riskInstructions = [480, 800]
riskDescriptions = [880, 560]

util = sorted(zip(utilCats, utilInstructions, utilDescriptions), key=lambda x: x[1] + x[2], reverse=True)
risk = sorted(zip(riskCats, riskInstructions, riskDescriptions), key=lambda x: x[1] + x[2], reverse=True)

utillabels = [x[0] for x in util]
utilinstructs = [x[1] for x in util]
utildescriptions = [x[2] for x in util]

risklabels = [x[0] for x in risk]
riskinstructs = [x[1] for x in risk]
riskdescriptions = [x[2] for x in risk]

# -- Utility -- #

x = np.arange(len(utillabels))
fig, ax = plt.subplots(figsize=figsize)

rects1 = ax.bar(x - barWidth/2, utilinstructs, barWidth, label='Instructive Utterances', color=set1)
rects2 = ax.bar(x + barWidth/2, utildescriptions, barWidth, label='Descriptive Utterances', color=set2)

ax.set_ylabel('Num of Utterances', fontsize=info)
ax.set_title('Instructions vs Descriptions by Utility', fontsize=title)
ax.set_xticks(x)
ax.set_xticklabels(utillabels, rotation=15, ha='right')
ax.legend()
ax.grid(axis='y', linestyle=linestyle, alpha=0.6)

ax.bar_label(rects1, padding=padding)
ax.bar_label(rects2, padding=padding)

fig.tight_layout()
plt.show()

# -- Risk -- #

x = np.arange(len(risklabels))
fig, ax = plt.subplots(figsize=figsize)

rects1 = ax.bar(x - barWidth/2, riskinstructs, barWidth, label='Instructive Utterances', color=set1)
rects2 = ax.bar(x + barWidth/2, riskdescriptions, barWidth, label='Descriptive Utterances', color=set2)

ax.set_ylabel('Num of Utterances', fontsize=info)
ax.set_title('Instructions vs Descriptions by Risk', fontsize=title)
ax.set_xticks(x)
ax.set_xticklabels(risklabels, rotation=15, ha='right')
ax.legend()
ax.grid(axis='y', linestyle=linestyle, alpha=0.6)

ax.bar_label(rects1, padding=padding)
ax.bar_label(rects2, padding=padding)

fig.tight_layout()
plt.show()

# -- Color vs Pattern -- #
labels = ["color gives less reward", "pattern gives less reward"]
color = [14, 29]
pattern = [25, 13]

x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=figsize)

rects1 = ax.bar(x - barWidth/2, color, barWidth, label='Color', color=set1)
rects2 = ax.bar(x + barWidth/2, pattern, barWidth, label='Pattern', color=set2)

ax.set_ylabel('Num of Utterances', fontsize=info)
ax.set_title('Focus of Instructive Utterances', fontsize=title)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.bar_label(rects1, padding=padding)
ax.bar_label(rects2, padding=padding)
fig.tight_layout()
plt.show()
