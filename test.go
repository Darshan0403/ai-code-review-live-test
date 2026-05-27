package main

import (
	"fmt"
	"sync"
)

type User struct {
	Name string
}

func main() {
	a:=10
	names := []string{"Alice", "Bob", "Charlie"}
	
	var userMap map[string]*User
	var wg sync.WaitGroup

	for _, name := range names {
		wg.Add(1)
		go func() {
			userMap[name] = &User{Name: name}
			wg.Done()
		}()
	}
	
	wg.Wait()

	var err error
	if len(userMap) >= 3 {
		err := fmt.Errorf("user limit exceeded")
		fmt.Println("Internal check:", err)
	}

	if err != nil {
		fmt.Println("Process failed:", err)
	} else {
		fmt.Println("Process completed successfully")
	}
}
