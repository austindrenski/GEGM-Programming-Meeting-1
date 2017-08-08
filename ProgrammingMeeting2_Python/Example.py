from functools import reduce
from AD_IO import read_delimited_file
from TradeData import TradeData

# Read the example trade data and pass a lambda function that constructs a TradeData object.
data = read_delimited_file("ExampleTradeData.txt", lambda x: TradeData(x[0], x[1], x[2], x[3], float(x[4])))

# Filter the source data into separate lists by source.
canData = list(filter(lambda x: x.source == "CAN", data))
mexData = list(filter(lambda x: x.source == "MEX", data))
usaData = list(filter(lambda x: x.source == "USA", data))

# Calculate the sum of the values where the source is CAN with list comprehension syntax.
sumCan0 = reduce(lambda current, next: current + next, [x.value for x in data if x.source == "CAN"])

# Calculate the sum of the values where the source is CAN with functional programming syntax.
sumCan1 = reduce(lambda current, next: current + next, map(lambda x: x.value, filter(lambda x: x.source == "CAN", data)))
