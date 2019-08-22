package main

import (
    "fmt"
    "log"
	"net/http"
	//"os"
    "github.com/gin-gonic/gin"
    "gopkg.in/olahol/melody.v1"
)

func main() {
	//port := os.Getenv("PORT")
  	/*if port == ""{
		log.Fatal("$PORT must be set")
	}*/
    log.Println("Websocket App start.")

    router := gin.Default()
    m := melody.New()

    rg := router.Group("/sampleapp")
    rg.GET("/", func(ctx *gin.Context) {
        http.ServeFile(ctx.Writer, ctx.Request, "index.html")
    })

    rg.GET("/ws", func(ctx *gin.Context) {
        m.HandleRequest(ctx.Writer, ctx.Request)
    })

    m.HandleMessage(func(s *melody.Session, msg []byte) {
        m.Broadcast(msg)
    })

    m.HandleConnect(func(s *melody.Session) {
        log.Printf("websocket connection open. [session: %#v]\n", s)
    })

    m.HandleDisconnect(func(s *melody.Session) {
        log.Printf("websocket connection close. [session: %#v]\n", s)
    })

    router.Run(":8080")

    fmt.Println("Websocket App End.")
}