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
	validPartOne := 0
	validPartTwo := 0
	for i := 0; i < len(lines); i++ {
		line := strings.Split(lines[i], " ")
		policy := strings.Split(line[0], "-")
		policyMin, _ := strconv.Atoi(policy[0])
		policyMax, _ := strconv.Atoi(policy[1])
		character := line[1][0:1]
		password := line[2]
		occurrences := strings.Count(password, character)
		if occurrences >= policyMin && occurrences <= policyMax {
			validPartOne++
		}
		if string(password[policyMin-1]) == character && string(password[policyMax-1]) != character {
			validPartTwo++
		} else if string(password[policyMin-1]) != character && string(password[policyMax-1]) == character {
			validPartTwo++
		}
	}
	fmt.Printf("Part one valid password #: %v \n", validPartOne)
	fmt.Printf("Part two valid password #: %v \n", validPartTwo)

}
