package main

import (
	"strconv"
	"fmt"
)

func isPalindrome(n int) bool{
	var istr = strconv.Itoa(n)
	mid := len(istr) / 2
	end := len(istr) - 1
	for i:=0; i < mid; i++ {
		if istr[i] != istr[end-i] {
			return false
		}
	}
	return true
}

func main() {
	for a := 999; a > 900; a-- {
		for b := 999; b > 900; b-- {
			if isPalindrome(a * b) {
				fmt.Println(a * b)
				return
			}
		}
	}
}