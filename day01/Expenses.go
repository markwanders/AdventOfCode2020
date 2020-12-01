package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func main() {
	dat, _ := ioutil.ReadFile(os.Args[1])
	lines := strings.Split(string(dat), "\n")
	for i := 0; i < len(lines)-1; i++ {
		a, _ := strconv.Atoi(lines[i])
		for j := 0; j < len(lines)-1; j++ {
			if j != i {
				b, _ := strconv.Atoi(lines[j])
				if a+b == 2020 {
					fmt.Printf("%v plus %v makes 2020\n", a, b)
					solution := a * b
					fmt.Printf("Multiply these values to get the solution: %v\n", solution)
					return
				}
			}
		}
	}
}
