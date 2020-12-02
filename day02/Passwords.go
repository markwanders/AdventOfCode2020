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
	valid := 0
	for i := 0; i < len(lines); i++ {
		line := strings.Split(lines[i], " ")
		policy := strings.Split(line[0], "-")
		policyMin, _ := strconv.Atoi(policy[0])
		policyMax, _ := strconv.Atoi(policy[1])
		character := line[1][0:1]
		password := line[2]
		occurrences := strings.Count(password, character)
		if occurrences >= policyMin && occurrences <= policyMax {
			valid++
		}
	}
	fmt.Printf("Valid password #: %v \n", valid)
}
