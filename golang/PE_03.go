package main

import(
	"fmt"
	"math"
)

const n int64 = 600851475143

func isPrime(n int64) bool {
	var p int64 = 2
	for ; p < n; p++ {
		if n % p == 0 { return false }
	}
  return true
}

func main() {
	var i int64 = int64(math.Sqrt(float64(n)))
	for ; i > 1; i-- {
		if n % i == 0 && isPrime(i) {
			fmt.Println(i)
			break
		}
	}
}