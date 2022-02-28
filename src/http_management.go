package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func FetchSiteWithCookie(url string) string {
	sturmSession, err := GetSturmSession(config.Hash)
	if err != nil {
		panic(err)
	}
	client := &http.Client{}
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		panic(err)
	}
	req.Header.Set("Cookie", "sturmsession="+sturmSession.Value)
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	site, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	return string(site)
}

func FetchSite(url string) string {
	resp, err := http.Get(url)
	defer resp.Body.Close()
	if err != nil {
		panic(err)
	}
	site, err := ioutil.ReadAll(resp.Body)
	return string(site)
}

func GetSturmSession(hash string) (*http.Cookie, error){
	url := fmt.Sprintf(
		"https://intranet.tam.ch/ksl/rest/ics/type/timetable/date/1642582786/auth/%s/calendar.ics",
		hash,
	)
	resp, err := http.Get(url)
	defer resp.Body.Close()
	if err != nil {
		return nil, fmt.Errorf(
			"error when getting cookie: %s",
			err,
		)
	}
	return resp.Cookies()[0], nil
}
