def batchData(data, batchSize=100):
    # Divide the stock lists in chunks of 100 (since iex allows batch api calls - max 100 symbols)
    # This line of code was provided by https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
    chunks = [data[x:x+batchSize]
              for x in range(0, len(data), batchSize)]

    # Create a list of chunks of stocks (in string form delimited by ',')
    batchList = []
    for i in range(0, len(chunks)):
        batchList.append(','.join(chunks[i]))

    return batchList
