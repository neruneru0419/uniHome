package main

import (
	"net/http"
	"io"
	"encoding/json"
	"fmt"
	"strconv"
	"os"
	"log"
)
func main(){
	port := os.Getenv("PORT")
	if port == ""{
		log.Fatal("$PORT must be set")
	}

	http.HandleFunc("/", handler)
	http.ListenAndServe(":"+port, nil)
}

func handler(w http.ResponseWriter, req *http.Request) {
	if req.Method != "POST" {
		w.WriteHeader(http.StatusBadRequest)
		return
	  }
	
	if req.Header.Get("Content-Type") != "application/json" {
	w.WriteHeader(http.StatusBadRequest)
	return
	}

	//To allocate slice for request body
	length, err := strconv.Atoi(req.Header.Get("Content-Length"))
	if err != nil {
	w.WriteHeader(http.StatusInternalServerError)
	return
	}

	//Read body data to parse json
	body := make([]byte, length)
	length, err = req.Body.Read(body)
	if err != nil && err != io.EOF {
	w.WriteHeader(http.StatusInternalServerError)
	return
	}

	//parse json
	var jsonBody map[string]interface{}
	err = json.Unmarshal(body[:length], &jsonBody)
	if err != nil {
	w.WriteHeader(http.StatusInternalServerError)
	return
	}
	fmt.Printf("%v\n", jsonBody)

	w.WriteHeader(http.StatusOK)  
	fmt.Fprintf(w, "Hello, %q", req.URL.Path[1:])
}