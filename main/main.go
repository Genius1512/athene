package main

import "fmt"

var config Config

func main() {
	var err error
	config, err = LoadConfig("../config.json")
	if err != nil {
		panic(err)
	}

	site, err := FetchSiteWithCookie("https://intranet.tam.ch/ksl/calendar")
	if err != nil {
		panic(err)
	}
	fmt.Println(site)
}
