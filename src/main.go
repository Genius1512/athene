package main

import "fmt"

var config Config

func main() {
	var err error
	config, err = LoadConfig("../config.json")
	if err != nil {
		panic(err)
	}

	site := FetchSite("https://intranet.tam.ch/ksl/calendar")
	fmt.Println(site)
}
