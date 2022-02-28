package main

import (
	"os"
	"encoding/json"
	"io/ioutil"
)

type Config struct {
	Hash string `json:"hash"`
}

func LoadConfig(filePath string) (Config, error) {
	file, err := os.Open("../config.json")
	if err != nil {
		return Config{}, err
	}
	bytes, err := ioutil.ReadAll(file)
	if err != nil {
		return Config{}, err
	}
	var config Config
	err = json.Unmarshal(bytes, &config)
	if err != nil {
		return Config{}, err
	}
	return config, nil
}
