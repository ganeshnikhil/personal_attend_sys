import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# def cl_plot(date_list , attendance_list , month , year):
#     # Convert the date list to pandas datetime format and create a DataFrame
#     df = pd.DataFrame({'Date': pd.to_datetime(date_list), 'Attendance': attendance_list})

#     # Extract day, weekday, and week number
#     df['Day'] = df['Date'].dt.day
#     df['Weekday'] = df['Date'].dt.weekday
#     df['Week'] = df['Date'].dt.isocalendar().week

#     # Create a pivot table to arrange days in a calendar format
#     pivot_table = df.pivot(index="Week", columns="Weekday", values="Attendance")
#     pivot_table = pivot_table.reindex(columns=range(7))
#     # Plotting the heatmap (calendar view)
#     plt.figure(figsize=(10, 6))
#     ax = sns.heatmap(pivot_table, annot=True, cmap='RdYlGn', cbar=False, linewidths=.5)

#     # Set labels and title
#     ax.set_yticklabels([f'Week {i}' for i in range(1, pivot_table.shape[0]+1)], rotation=0)
#     ax.set_xticklabels(list(calendar.day_name), rotation=45)
#     plt.title(f'Student Attendance Calendar - {month} {year}')
#     path = f"Month/{month}.png"
#     plt.savefig(path)
#     return path  


def cl_plot(date_list, attendance_list, month, year):
    # Convert the date list to pandas datetime format and create a DataFrame
    df = pd.DataFrame({'Date': pd.to_datetime(date_list), 'Attendance': attendance_list})

    # Extract day, weekday, and week number
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.weekday
    df['Week'] = df['Date'].dt.isocalendar().week

    # Create a pivot table for attendance (0 and 1) to arrange days in a calendar format
    pivot_table = df.pivot(index="Week", columns="Weekday", values="Attendance")

    # Create a pivot table for the day of the month for annotations
    day_labels = df.pivot(index="Week", columns="Weekday", values="Day").fillna(0).astype(int)

    # Ensure the pivot table has 7 columns (for each day of the week)
    pivot_table = pivot_table.reindex(columns=range(7))
    day_labels = day_labels.reindex(columns=range(7))

    # Plotting the heatmap (calendar view)
    plt.figure(figsize=(10, 6))
    ax = sns.heatmap(pivot_table, annot=day_labels, fmt='', cmap='RdYlGn', cbar=False, linewidths=.5, linecolor='black')

    # Set labels and title
    ax.set_yticklabels([f'Week {i}' for i in range(1, pivot_table.shape[0] + 1)], rotation=0)
    ax.set_xticklabels(list(calendar.day_name), rotation=45)
    plt.title(f'Student Attendance Calendar - {month} {year}')

    # Save the plot to a file
    path = f"Month/{month}_{year}.png"
    plt.savefig(path)
    
    return path

# import matplotlib.pyplot as plt

# # Plot bar graph
# plt.bar(list1, list2)
# plt.xlabel('List 1 (0 to 12)')
# plt.ylabel('List 2 (Random values)')
# plt.title('Bar Graph of List 1 vs Random Values from List 2')
# plt.show()

def br_plot(months, days_present, year):
    # Create the bar plot with no space between bars
    plt.figure(figsize=(10, 6))

    # Ensure the bars are spaced tightly by setting width to 1.0
    plt.bar(months, days_present, width=0.9 , color="green")

    # Add labels and title
    plt.xlabel('Month')
    plt.ylabel('Days Present')
    plt.title('Student Attendance by Month')

    # Ensure months are passed as valid tick positions for x-axis
    plt.xticks(months, labels=months, rotation=45)

    # Adjust layout to remove extra spaces
    

    # Save plot to file
    path = f"YEAR/{year}.png"
    plt.savefig(path)
    return path

def cl_plot(date_list, attendance_list, month, year):
    # Convert the date list to pandas datetime format and create a DataFrame
    df = pd.DataFrame({'Date': pd.to_datetime(date_list), 'Attendance': attendance_list})

    # Extract day, weekday, and week number
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.weekday
    df['Week'] = df['Date'].dt.isocalendar().week

    # Create a pivot table for attendance (0 and 1) to arrange days in a calendar format
    pivot_table = df.pivot(index="Week", columns="Weekday", values="Attendance")

    # Create a pivot table for the day of the month for annotations
    day_labels = df.pivot(index="Week", columns="Weekday", values="Day").fillna(0).astype(int)

    # Ensure the pivot table has 7 columns (for each day of the week)
    pivot_table = pivot_table.reindex(columns=range(7))
    day_labels = day_labels.reindex(columns=range(7))

    # Plotting the heatmap (calendar view)
    plt.figure(figsize=(10, 6))
    ax = sns.heatmap(pivot_table, annot=day_labels, fmt='', cmap='RdYlGn', cbar=False, linewidths=.5, linecolor='black')

    # Set labels and title
    ax.set_yticklabels([f'Week {i}' for i in range(1, pivot_table.shape[0] + 1)], rotation=0)
    ax.set_xticklabels(list(calendar.day_name), rotation=45)
    plt.title(f'Student Attendance Calendar - {month} {year}')

    # Save the plot to a file
    path = f"Month/{month}_{year}.png"
    plt.savefig(path)
    
    return path
