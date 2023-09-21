package kata

func century(year int) int {
	return (year + 99) / 100 // For example if the year is 1901, it's the 20th century,
	// but doing `year / 100` would result in it being the 19th,
	// so adding 99 would move it to the next century
}
