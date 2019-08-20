package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)
func main(){
	port := os.Getenv("PORT")
	if port == ""{
		log.Fatal("$PORT must be set")
	}

	http.HandleFunc("/", handler)
	http.ListenAndServe(":"+port, nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %q", r.URL.Path[1:])
}