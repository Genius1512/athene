package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func FetchSiteWithCookie(url string) (string, error) {
	sturmSession, err := GetSturmSession(config.Hash)
	if err != nil {
		return "nil", err
	}
	client := &http.Client{}
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return "nil", err
	}
	req.Header.Set("Cookie", "sturmsession="+sturmSession)
	resp, err := client.Do(req)
	if err != nil {
		return "nil", err
	}
	defer resp.Body.Close()

	text, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "nil", err
	}

	return string(text), nil
}

func GetSturmSession(hash string) (string, error){
	url := fmt.Sprintf(
		"https://intranet.tam.ch/ksl/rest/ics/type/timetable/date/1642582786/auth/%s/calendar.ics",
		hash,
	)
	resp, err := http.Get(url)
	defer resp.Body.Close()
	if err != nil {
		return "nil", fmt.Errorf(
			"error when getting cookie: %s",
			err,
		)
	}
	return resp.Cookies()[0].Value, nil
}
