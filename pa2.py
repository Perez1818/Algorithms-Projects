#Estefania Perez
import csv 
import sys

def knapsack(weights, values, max_w):
  n = len(weights)
  #2D table is made
  table_list = [[0 for x in range(max_w + 1)] for x in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(max_w + 1):
      if weights[i - 1] <= j:
        table_list[i][j] = max(table_list[i - 1][j], table_list[i - 1][j - weights[i - 1]] + values[i - 1])
      else:
        table_list[i][j] = table_list[i - 1][j]

  taken_items = []
  w = max_w
  for i in range(n, 0, -1):
    if table_list[i][w] != table_list[i - 1][w]:
      taken_items.append(weights[i-1])
      w -= weights[i - 1]

  return table_list[n][max_w], taken_items
  


if __name__ == "__main__":

  if len(sys.argv) != 3:
    print("Usage: python pa2.py <csv_filename> <cart_capacity>")
    sys.exit(1)
  filename = sys.argv[1]
  max_weight = int(sys.argv[2])

  final_weights = []
  final_values = []

  with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      if row:
        num1, num2 = row
        #first column is weight
        #Second column is value
        weight = int(num1)
        value = int(num2)
        if weight <= max_weight:
          final_weights.append(weight)
          final_values.append(value)

  max_value, selected_weights = knapsack(final_weights, final_values, max_weight)

  print(f"Max value of items taken is {max_value}. Array of weights of items taken is {selected_weights}")


