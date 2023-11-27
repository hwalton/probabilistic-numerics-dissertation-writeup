# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from datetime import datetime, timedelta
#
# start_date = datetime(2023, 12, 18)
# end_date = datetime(2024, 6, 3)
#
# semester_weeks = [
#     ('XMAS BREAK', start_date, datetime(2024, 2, 4)),
#     ('Week 1', datetime(2024, 2, 5), datetime(2024, 2, 11)),
#     ('Week 2', datetime(2024, 2, 12), datetime(2024, 2, 18)),
#     ('Week 3', datetime(2024, 2, 19), datetime(2024, 2, 18)),
#     ('Week 4', datetime(2024, 2, 26), datetime(2024, 2, 18)),
#     ('Week 5', datetime(2024, 3, 4), datetime(2024, 2, 18)),
#     ('Week 6', datetime(2024, 3, 11), datetime(2024, 2, 18)),
#     ('Week 7', datetime(2024, 3, 18), datetime(2024, 2, 18)),
#     ('Week 8', datetime(2024, 2, 12), datetime(2024, 2, 18)),
#     ('EASTER BREAK', datetime(2024, 3, 19), datetime(2024, 4, 14)),
#     # ... continue after Easter break
#     ('Week 10', datetime(2024, 5, 27), end_date)
# ]
#
# # Define the tasks
# tasks = [
#     "Adjust the model to enable the closed form Fourier Transform to be found.",
#     "Compare the noise resilience with the existing discrete Fast Fourier Transform.",
#     "FRF computed for both methods.",
#     "Compute MSE between the two",
#     "Add Gaussian Noise and compare MSE of unmodified vs noise for both methods",
#     "Repeat for new signal of pure sine wave",
#     "Write up conclusions in report"
# ]
#
# # Create figure and plot space
# plt.figure(figsize=(15, 8))
#
# # Create a list for the y-axis labels
# y_labels = []
#
# # Initialize the start date for the first task
# current_start_date = None
#
# # Plot each task
# for i, task in enumerate(tasks):
#     # Find the start and end dates for each task
#     for week_name, week_start, week_end in semester_weeks:
#         if week_name in ['XMAS BREAK', 'EASTER BREAK']:
#             continue
#         if current_start_date is None or current_start_date < week_start:
#             current_start_date = week_start
#             break
#
#     # Add the task as a bar in the Gantt chart
#     plt.barh(i, (week_end - week_start).days, left=(week_start - start_date).days, color='skyblue')
#
#     # Update the start date for the next task
#     current_start_date = week_end + timedelta(days=1)
#
#     # Add the task name to y_labels
#     y_labels.append(task)
#
# # Set the y-axis labels
# plt.yticks(range(len(y_labels)), y_labels)
#
# # Format the x-axis to show dates
# plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MONDAY))
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
# plt.gca().set_xlim(start_date, end_date)
#
# # Rotate date labels for better readability
# plt.xticks(rotation=90)
#
# # Add gridlines
# plt.grid(True)
#
# # Save the figure
# plt.tight_layout()
# plt.savefig('gantt_chart.png')
#
# # Show the plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Define the start and end dates for the chart
start_date = datetime(2023, 12, 18)
end_date = datetime(2024, 6, 3)

# Define the semester weeks and breaks
dates = [
    ('XMAS BREAK', start_date, datetime(2024, 2, 4)),
    ('Week 1', datetime(2024, 2, 5), datetime(2024, 2, 11)),
    ('Week 2', datetime(2024, 2, 12), datetime(2024, 2, 18)),
    # ... continue for all weeks
    ('EASTER BREAK', datetime(2024, 3, 19), datetime(2024, 4, 14)),
    # ... continue after Easter break
    ('Week 10', datetime(2024, 5, 27), end_date)
]

# Create a DataFrame
df = pd.DataFrame(dates, columns=['Task', 'Start', 'Finish'])

# Create figure and plot space
plt.figure(figsize=(10, 6))

# Plot each task
for i, row in df.iterrows():
    plt.barh(row['Task'], (row['Finish'] - row['Start']).days, left=(row['Start'] - start_date).days, color='skyblue')

# Format the x-axis to show dates
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MONDAY))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
plt.gca().set_xlim(start_date, end_date)

# Rotate date labels for better readability
plt.xticks(rotation=90)

# Add gridlines
plt.grid(True)

# Save the figure
plt.tight_layout()
plt.savefig('gantt-chart_.png')

# Show the plot
plt.show()

