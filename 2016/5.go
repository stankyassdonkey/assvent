package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
)

func main() {

	input := "wtnhxymk"
	password := ""
	index := 0

	for len(password) < 8 {
		id := input + fmt.Sprint(index)
		hash := GetMd5Hash(id)

		if hash[:5] == "00000" {
			password += string(hash[5])
		}

		index++
		fmt.Println(index, password)
	}
}

func GetMd5Hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}
