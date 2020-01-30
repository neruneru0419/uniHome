package com.example.mainscreen

import com.squareup.moshi.Json

data class User(
    var name: String,
    var age: Int,
    @field:Json(name = "last_update")   // @Json(name = "last_update")
    var lastUpdate: Long                // ↑これだと、変換されなかった
)