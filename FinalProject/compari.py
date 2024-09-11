import matplotlib.pyplot as plt
import pandas as pd

# Load the Excel file
file_path = 'data.xlsx'
data = pd.ExcelFile(file_path)

# Read the sheets
sheet1 = data.parse(sheet_name=0)
sheet2 = data.parse(sheet_name=1)

# Prepare data for plotting
sheet1_x1 = sheet1['nodes']
sheet1_y1_1 = sheet1['delay(k-means)/ns']
sheet1_y1_2 = sheet1['delay(aodv)/ns']
sheet1_y2_1 = sheet1['delivery ratio(k-means)']
sheet1_y2_2 = sheet1['delivery ratio(aodv)']

sheet2_x1 = sheet2['pps']
sheet2_y1_1 = sheet2['delay(k-means)/ns']
sheet2_y1_2 = sheet2['delay(aodv)/ns']
sheet2_y2_1 = sheet2['delivery ratio(k-means)']
sheet2_y2_2 = sheet2['delivery ratio(aodv)']

# Plotting the first sheet with specific colors
plt.figure(figsize=(14, 10))

# Plot for delay comparison
# plt.subplot(2, 1, 1)
plt.plot(sheet1_x1, sheet1_y1_1/1e8, 'r', label='delay(k-means)/ns')
plt.plot(sheet1_x1, sheet1_y1_2/1e8, 'b', label='delay(aodv)/ns')
plt.xlabel('nodes')
plt.ylabel('delay (ns)')
plt.title('Sheet 1: Delay Comparison')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 10))

# Plot for delivery ratio comparison
# plt.subplot(2, 1, 2)
plt.plot(sheet1_x1, sheet1_y2_1, 'r', label='delivery ratio(k-means)')
plt.plot(sheet1_x1, sheet1_y2_2, 'b', label='delivery ratio(aodv)')
plt.xlabel('nodes')
plt.ylabel('delivery ratio')
plt.title('Sheet 1: Delivery Ratio Comparison')
plt.legend()

plt.tight_layout()
plt.show()

# Plotting the second sheet with specific colors
plt.figure(figsize=(14, 10))

# Plot for delay comparison
# plt.subplot(2, 1, 1)
plt.plot(sheet2_x1, sheet2_y1_1/1e8, 'r', label='delay(k-means)/ns')
plt.plot(sheet2_x1, sheet2_y1_2/1e8, 'b', label='delay(aodv)/ns')
plt.xlabel('pps')
plt.ylabel('delay (ns)')
plt.title('Sheet 2: Delay Comparison')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 10))

# Plot for delivery ratio comparison
# plt.subplot(2, 1, 2)
plt.plot(sheet2_x1, sheet2_y2_1, 'r', label='delivery ratio(k-means)')
plt.plot(sheet2_x1, sheet2_y2_2, 'b', label='delivery ratio(aodv)')
plt.xlabel('pps')
plt.ylabel('delivery ratio')
plt.title('Sheet 2: Delivery Ratio Comparison')
plt.legend()

plt.tight_layout()
plt.show()
