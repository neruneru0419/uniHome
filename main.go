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
	log.Println("Websocket App start.")

	router := gin.Default()
	m := melody.New()
	rg := router.Group("/uniHome")

	rg.GET("/ws", func(ctx *gin.Context) {
		m.HandleRequest(ctx.Writer, ctx.Request)
	})

	m.HandleMessage(func(s *melody.Session, msg []byte) {
		var uniboData uniboLog.UniboData
		m.Broadcast(msg)
		json.Unmarshal(msg, &uniboData)
		uniboLog.WriteLog(uniboData)
		fmt.Println(uniboData.Words)
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
