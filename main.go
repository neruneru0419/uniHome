package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
)
type Unibo struct {
	Id   int    `json:"id"`
	Name string `json:"name"`
}

func handleUniboJson(w http.ResponseWriter, r *http.Request) {
	// header
	method := r.Method
	fmt.Println("[method] " + method)
	for k, v := range r.Header {
		fmt.Print("[header] " + k)
		fmt.Println(": " + strings.Join(v, ","))
	}

	// POST (json)
	if method == "POST" {
		defer r.Body.Close()
		body, err := ioutil.ReadAll(r.Body)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println("[request body row] " + string(body))

		var unibo Unibo
		error := json.Unmarshal(body, &unibo)
		if error != nil {
			log.Fatal(error)
		}
		fmt.Printf("[request body decoded] %+v\n", unibo)
		fmt.Fprint(w, string(body))
		//postAsJson()
	}
}

func postAsJson() {
	// json values
	values, err := json.Marshal(Unibo{Id: 1, Name: "UniboA"})

	res, err := http.Post("http://localhost:8080/", "application/json", bytes.NewBuffer(values))
	if err != nil {
		log.Fatal(err)
	}

	// header
	fmt.Printf("[status] %d\n", res.StatusCode)
	for k, v := range res.Header {
		fmt.Print("[header] " + k)
		fmt.Println(": " + strings.Join(v, ","))
	}

	// body
	defer res.Body.Close()
	body, error := ioutil.ReadAll(res.Body)
	if error != nil {
		log.Fatal(error)
	}
	fmt.Println("[body] " + string(body))
}

func main(){
	http.HandleFunc("/", handleUniboJson)
	http.ListenAndServe(":8080", nil)
}