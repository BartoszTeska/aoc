package second

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getDataReader(filename string) *bufio.Scanner {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(err.Error())
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	return scanner
}

func parseData(scanner *bufio.Scanner) [][]int {
	var arr [][]int
	for scanner.Scan() {
		line := scanner.Text()
		splitLine := strings.Split(line, " ")
		numsArr := make([]int, 0)
		for _, num := range splitLine {
			parsedNumber, err := strconv.Atoi(num)
			if err != nil {
				panic(err)
			}
			numsArr = append(numsArr, parsedNumber)
		}
		arr = append(arr, numsArr)
	}

	return arr
}

func distance(a, b int) int {
	return b - a
}

func solution(numbers [][]int) int {
	var sum int = 0
	for _, line := range numbers {
		for i := range line {
			if i == len(line) {
				break
			}
			a, b := line[i], line[i+1]
		}
	}

	return 1
}

func SolutionPrinter() {
	fmt.Println("--- Day 2 ---")
}
