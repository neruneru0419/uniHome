package main

import (
	"fmt"
	"log"
	"os"
	"io/ioutil"

	"github.com/gin-gonic/autotls"
	"github.com/gin-gonic/gin"
	"gopkg.in/olahol/melody.v1"
)
func Fileread(){
	file, err := os.Open("./UniboLog.txt")
	if err != nil{
		fmt.Println("FileReadError")
	}
	defer file.Close()

	log, err := ioutil.ReadAll(file)

	return string(log)
}

func main() {
	log.Println("Websocket App start.")

	router := gin.Default()
	m := melody.New()

	rg := router.Group("/uniHome")

	rg.GET("/ws", func(ctx *gin.Context) {
		m.HandleRequest(ctx.Writer, ctx.Request)
	})
	rg.GET("/api/log", func(ctx *gin.Context) {
		log = Fileread()
		ctx.JSON(200, gin.H{
			"message": log,
		})
	})
	rg.GET("/api/reaction", func(ctx *gin.Context) {
		ctx.JSON(200, gin.H{
			"message": "hello, world",
		})
	})
	rg.POST("/api/action", func(ctx *gin.Context) {
		ctx.JSON(200, gin.H{
			"message": "hello, world",
		})
	})

	m.HandleMessage(func(s *melody.Session, msg []byte) {
		m.Broadcast(msg)
		fmt.Println(msg)
	})

	m.HandleConnect(func(s *melody.Session) {
		log.Printf("websocket connection open. [session: %#v]\n", s)
	})

	m.HandleDisconnect(func(s *melody.Session) {
		log.Printf("websocket connection close. [session: %#v]\n", s)
	})

	log.Fatal(autotls.Run(router, "neruneru.higashi.dev"))

	fmt.Println("Websocket App End.")
}
