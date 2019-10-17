
package main

import (
        "encoding/json"
        "fmt"
        "log"
        "io/ioutil"
        "./uniboLog"
        "github.com/gin-gonic/gin"
        "gopkg.in/olahol/melody.v1"
)

func main() {
        log.Println("uniHome Server Start.")

        router := gin.Default()
        m := melody.New()
        rg := router.Group("/uniHome")
        rg.GET("/ws", func(ctx *gin.Context) {
                m.HandleRequest(ctx.Writer, ctx.Request)
        })

        m.HandleMessage(func(s *melody.Session, msg []byte){
			var uniboData uniboLog.UniboData
			json.Unmarshal(msg, &uniboData)
			if uniboData.IsLog{
				bytes, _ := ioutil.ReadFile("log.json")
				m.Broadcast(bytes)
			}else{
				m.Broadcast(msg)
			}
			if uniboData.HeadSensor || uniboData.HumanSensor || uniboData.Greeting{
				uniboLog.WriteLog(uniboData)
			}
			fmt.Println(uniboData.HeadSensor, uniboData.HumanSensor, uniboData.Greeting)
		})

		m.HandleConnect(func(s *melody.Session) {
				log.Printf("websocket connection open. [session: %#v]\n", s)
		})

		m.HandleDisconnect(func(s *melody.Session) {
				log.Printf("websocket connection close. [session: %#v]\n", s)
		})
		router.Run(":8080")

		fmt.Println("uniHome Server End.")
}
	
	
