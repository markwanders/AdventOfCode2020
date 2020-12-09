package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type Instruction struct {
	Operation string
	Argument  int
}

func main() {
	var instructions []Instruction
	for _, line := range readInput() {
		split := strings.Split(line, " ")
		argument, _ := strconv.Atoi(split[1])
		instructions = append(instructions, Instruction{split[0], argument})
	}
	_, part1 := runProgram(instructions)
	println(part1)
	println(fixProgram(instructions))
}

func runProgram(instructions []Instruction) (int, int) {
	accumulator := 0
	seen := make(map[int]bool)
	for i := 0; i <= len(instructions); i++ {
		if i == len(instructions) {
			return 0, accumulator
		} else if seen[i] {
			return 1, accumulator
		}
		seen[i] = true
		instruction := instructions[i]
		switch instruction.Operation {
		case "acc":
			accumulator += instruction.Argument
		case "jmp":
			i += instruction.Argument - 1
		}
	}
	return 1, accumulator
}

func fixProgram(instructions []Instruction) int {
	for index, instruction := range instructions {
		changed := make([]Instruction, len(instructions))
		switch instruction.Operation {
		case "jmp":
			copy(changed, instructions)
			changed[index].Operation = "nop"
		case "nop":
			copy(changed, instructions)
			changed[index].Operation = "jmp"
		default:
			continue
		}
		exitCode, result := runProgram(changed)
		if exitCode == 0 {
			return result
		}
	}
	return 0
}

func readInput() []string {
	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var data []string

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return data
}
