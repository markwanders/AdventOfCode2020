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
		for j := i + 1; j < len(lines)-1; j++ {
			b, _ := strconv.Atoi(lines[j])
			if a+b == 2020 {
				fmt.Printf("%v plus %v makes 2020\n", a, b)
				solution := a * b
				fmt.Printf("Multiply these values to get the solution to part 1: %v\n", solution)
				break
			} else if a+b < 2020 {
				for k := j + 1; k < len(lines)-1; k++ {
					c, _ := strconv.Atoi(lines[k])
					if a+b+c == 2020 {
						fmt.Printf("%v plus %v plus %v makes 2020\n", a, b, c)
						solution := a * b * c
						fmt.Printf("Multiply these values to get the solution to part 2: %v\n", solution)
						break
					}
				}
			}
		}
	}
}
