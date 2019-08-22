package main

import (
    "fmt"
    "log"
	"net/http"
    "github.com/gin-gonic/gin"
    "gopkg.in/olahol/melody.v1"
)

func main() {
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

    // Listen and server on 0.0.0.0:80
    
    router.Run(":80")

    fmt.Println("Websocket App End.")
}