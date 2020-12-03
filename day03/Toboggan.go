package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	dat, _ := ioutil.ReadFile(os.Args[1])
	lines := strings.Split(string(dat), "\n")
	slopes := [][]int{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}
	answer := 1
	for _, slope := range slopes {
		trees := 0
		x := 0
		for y := 0; y < len(lines); y += slope[1] {
			if string(lines[y][x]) == "#" {
				trees += 1
			}
			x += slope[0]
			x %= len(lines[y])
		}
		fmt.Printf("Trees for slope [%v %v]: %v\n", slope[0], slope[1], trees)
		answer *= trees
	}
	println(answer)
}
