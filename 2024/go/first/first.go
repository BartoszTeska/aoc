package first

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"regexp"
	"slices"
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

func parseData(scanner *bufio.Scanner) ([]int, []int) {
	var arr []string
	var left, right []int
	arr = make([]string, 0)
	for scanner.Scan() {
		arr = append(arr, scanner.Text())
	}
	for _, line := range arr {
		regex := regexp.MustCompile(`\s{1,}`)
		fixedLine := regex.ReplaceAllString(line, " ")
		nums := strings.Split(fixedLine, " ")
		leftNum, _ := strconv.Atoi(nums[0])
		rightNum, _ := strconv.Atoi(nums[1])
		left = append(left, leftNum)
		right = append(right, rightNum)
	}
	slices.Sort(left)
	slices.Sort(right)

	return left, right
}

func solution(left, right []int) int {
	sum := 0
	for i := range left {
		distance := int(math.Abs(float64(right[i]) - float64(left[i])))
		sum += distance
	}

	return sum
}

func countElementsEqual(arr []int, element int) int {
	count := 0
	for _, v := range arr {
		if v == element {
			count += 1
		}
	}
	return count
}

func solution2(left, right []int) int {
	sum := 0
	for _, v := range left {
		count := countElementsEqual(right, v)
		if count == 0 {
			continue
		}
		sum += v * count
	}
	return sum
}

func SolutionPrinter(filepath string) {
	scanner := getDataReader(filepath)
	left, right := parseData(scanner)
	fmt.Println("--- Day 1 ---")
	fmt.Println("part1: ", solution(left, right))
	fmt.Println("part2: ", solution2(left, right))
}
