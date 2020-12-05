package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
	"strings"
)

func main() {
	dat, _ := ioutil.ReadFile(os.Args[1])
	seats := strings.Split(string(dat), "\n")
	var seatIDs []int
	highestSeatID := 0
	for _, seat := range seats {
		rows := make([]int, 128)
		for i := range rows {
			rows[i] = i
		}
		columns := make([]int, 8)
		for i := range columns {
			columns[i] = i
		}
		for _, c := range seat {
			if c == 'F' {
				rows = rows[:len(rows)/2]
			} else if c == 'B' {
				rows = rows[len(rows)/2:]
			} else if c == 'L' {
				columns = columns[:len(columns)/2]
			} else if c == 'R' {
				columns = columns[len(columns)/2:]
			}
		}
		var seatID = rows[0]*8 + columns[0]
		seatIDs = append(seatIDs, seatID)
		if seatID > highestSeatID {
			highestSeatID = seatID
		}

	}
	fmt.Printf("highest seat id %v\n", highestSeatID)
	sort.Ints(seatIDs)
	for index, seatID := range seatIDs {
		if seatIDs[index+1] != seatID+1 {
			fmt.Printf("Found missing seatID %v\n", seatID+1)
			break
		}
	}

}
