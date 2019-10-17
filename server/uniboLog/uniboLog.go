package uniboLog

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"time"
)
type UniboData struct {
	Type        string `json:"type"`
	User        string `json:"user"`
	HumanSensor bool   `json:"human_sensor"`
	HeadSensor  bool   `json:"head_sensor"`
	Greeting    bool   `json:"greeting"`
	Words       string `json:"words"`
	IsLog       bool   `json:"isLog"`
}
func getTime() string {
	t := time.Now()
	hour := strconv.Itoa(t.Hour())
	minute := strconv.Itoa(t.Minute())
	fmt.Println(len(hour))
	if len(hour) == 1{
		hour = "0" + hour
	}
	if len(minute) == 1{
		minute = "0" + minute
	}
	nowTime := (hour + ":" + minute)

	return nowTime
}
func getName(name string) string {
	var user string
	if name == "child" {
		user = "こども"
	} else if name == "parents" {
		user = "りょうしん"
	} else if name == "grand_parents" {
		user = "そふぼ"
	}
	return user
}
func getAction(uniboData UniboData) string {
	var messageLog string
	if uniboData.HeadSensor {
		messageLog = ("ゆにぼのあたまを撫でました")
	} else if uniboData.HumanSensor {
		messageLog = ("ゆにぼの近くを通りました")
	} else if uniboData.Greeting {
		messageLog = ("「" + uniboData.Words + "」" + "と挨拶をしました")
	}

	return messageLog
}
func WriteLog(uniboData UniboData) {
	bytes, err := ioutil.ReadFile("log.json")
	fmt.Println(bytes)
	if err != nil {
		log.Fatal(err)
	}
	nowTime := getTime()
	name := getName(uniboData.User)
	action := getAction(uniboData)
	logs := "	{\n		\"name\": \"" + name + "\",  \n		\"time\": \"" + nowTime + "\", \n		\"log\": \"" + action + "\"\n	}\n"
	lastWord := len(bytes) - 2
	content := []byte(string(bytes)[:lastWord] + ",\n" + logs + "]")
	ioutil.WriteFile("log.json", content, os.ModePerm)
}

