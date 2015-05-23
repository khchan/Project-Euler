package main

import "fmt"

func main() {
	cache, i, sum := []int{1, 1}, 0, 0
	for i < 4e6 {
		i = cache[0] + cache[1]; cache[0] = cache[1]; cache[1] = i
		if i % 2 == 0 {
			sum += i
		}
	}
	fmt.Printf("Sum of all even fib terms: %d\n", sum)
}
