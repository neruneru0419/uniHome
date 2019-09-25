package main

import (
	"encoding/json"
	"fmt"
	"log"

	"./uniboLog"
	"github.com/gin-gonic/autotls"
	"github.com/gin-gonic/gin"
	"gopkg.in/olahol/melody.v1"
)

func main() {
	log.Println("uniHome Server Start.")

	router := gin.Default()
	m := melody.New()
	rg := router.Group("/uniHome")
	var uniboData uniboLog.UniboData
	rg.GET("/ws", func(ctx *gin.Context) {
		m.HandleRequest(ctx.Writer, ctx.Request)
	})

	m.HandleMessage(func(s *melody.Session, msg []byte) {
		m.Broadcast(msg)
		json.Unmarshal(msg, &uniboData)
		if uniboData.HeadSensor || uniboData.HumanSensor || uniboData.Greeting{
			uniboLog.WriteLog(uniboData)
		}
	})

	m.HandleConnect(func(s *melody.Session) {
		log.Printf("websocket connection open. [session: %#v]\n", s)
	})

	m.HandleDisconnect(func(s *melody.Session) {
		log.Printf("websocket connection close. [session: %#v]\n", s)
	})

	log.Fatal(autotls.Run(router, "neruneru.higashi.dev"))

	fmt.Println("uniHome Server End.")
}
