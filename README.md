# oracolo
Signal buy, hold, sell and wait opportunities on stocks and cryptos

## Algorithm:

### Inputs

Symbol `sy`

Frequency (days, hours, etc)


### Fill backlog of values

1. Fetch the indicators, sorted by domain width, descending

2. Let `ww` be the width of the widest indicator
3. Let `lvt` be the timestamp of when the given symbol was last fetched
4. Fetch and save the values for the given symbol in the time range
	(`st := max(now - ww, lvt)`, `now`]

### Housekeeping

Delete all values older than `st` (for any symbol)

### Calculate indicators

1. Let `vals` be all the values for the symbol (sorted if necessary)

2. For each indicator (sorted by width, as fetched above):
	- let `iw` be its width
	- let `vi` be the value of the indicator function applied to the subset
		`vals[-iw:]`
	- let `si` be the indicator signal applied to the `vals[-1]` and `vi` 
	- show `vals[-1]`, `vi`, `si`
