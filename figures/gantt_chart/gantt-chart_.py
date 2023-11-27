import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

plt.rcParams.update({'font.size': 12})

df = pd.DataFrame({
    'task': ['XMAS HOLIDAY AND EXAM PERIOD',
             'Adjust the model to enable the closed\nform Fourier Transform to be found.',
             'Compute FRF for both methods.',
             'Compute MSE between\nthe two methods.',
             'Add Gaussian Noise\nand compare the MSE.',
             'Repeat for new signal\nof pure sine wave.',
             'EASTER HOLIDAY',
             'Write up conclusions\nin report.'],
    'start': pd.to_datetime(['18 DEC 2023', '5 FEB 2024', '19 FEB 2024', '4 MAR 2024', '11 MAR 2024', '18 MAR 2024', '25 MAR 2024', '15 APR 2024'], format='%d %b %Y'),
    'end': pd.to_datetime(['4 FEB 2024', '18 FEB 2024', '3 MAR 2024', '10 MAR 2024', '17 MAR 2024', '24 MAR 2024', '14 APR 2024', '1 MAY 2024'], format='%d %b %Y')
})

df['days_to_start'] = (df['start'] - df['start'].min()).dt.days
df['days_to_end'] = (df['end'] - df['start'].min()).dt.days
df['task_duration'] = df['days_to_end'] - df['days_to_start'] + 1

fig, ax = plt.subplots(figsize=(10, 6))

for i in range(len(df)):
    color = 'red' if df.iloc[i]['task'] in ['XMAS HOLIDAY AND EXAM PERIOD', 'EASTER HOLIDAY'] else 'blue'
    ax.barh(y=df.iloc[i]['task'], width=df.iloc[i]['task_duration'], left=df.iloc[i]['days_to_start'], color=color)

ax.invert_yaxis()

ax.set_title('Future Work Time Plan', fontsize=15)

start_date = df['start'].min()
end_date = df['end'].max()

extended_end_date = max(end_date, df['end'].max()) + pd.Timedelta(days=7)
mondays = pd.date_range(start=start_date, end=extended_end_date, freq='W-MON')

xticks = (mondays - start_date).days
xticklabels = mondays.strftime("%d %b %y")

ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels, rotation=90)

ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')

deadline = dt.datetime(2024, 5, 2)
deadline_days = (deadline - df['start'].min()).days
ax.axvline(x=deadline_days, color='red', linestyle='dotted', lw=2)

ax.text(deadline_days + 1, 0.5, 'REPORT DUE 2 MAY 24', rotation=90, verticalalignment='center_baseline', horizontalalignment='left', color='red')

ax.xaxis.grid(True, alpha=0.5)

plt.tight_layout()
plt.savefig('gantt-chart_.png')
plt.show()


