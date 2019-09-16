package com.example.mainscreen

import android.os.Bundle
import android.os.Handler
import android.provider.Settings
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.view.View
import android.view.animation.AnimationUtils
import android.widget.ImageButton
import android.widget.ImageView
import com.example.mainscreen.R.layout.activity_main
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    private val handler = Handler()
    private var eye_animation = Runnable {}
    private var heart_animation = Runnable {}
    private var puff_animation = Runnable {}
    private var dance_animation_parents = Runnable {}
    private var dance_animation_grandparents = Runnable{}
    private var greeting_animation1_parents = Runnable{}
    private var greeting_animation2_parents = Runnable{}
    private var greeting_animation3_parents = Runnable{}
    private var greeting_animation1_grandparents = Runnable{}
    private var greeting_animation2_grandparents = Runnable{}
    private var greeting_animation3_grandparents = Runnable{}
    private var notification_parents = Runnable{}
    private var notification_grandparents = Runnable{}


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(activity_main)

        var flag = true
        val unibo_2 = findViewById<ImageView>(R.id.unibo_2)
        val goodmorning_1_parents = findViewById<ImageView>(R.id.goodmorning_1_parents)
        val goodmorning_2_parents = findViewById<ImageView>(R.id.goodmorning_2_parents)
        val goodnight_1_parents = findViewById<ImageView>(R.id.goodnight_1_parents)
        val goodnight_2_parents = findViewById<ImageView>(R.id.goodnight_2_parents)
        val welcomehome_1_parents = findViewById<ImageView>(R.id.welcomehome_1_parents)
        val welcomehome_2_parents = findViewById<ImageView>(R.id.welcomehome_2_parents)
        val goodmorning_1_grandparents = findViewById<ImageView>(R.id.goodmorning_1_grandparents)
        val goodmorning_2_grandparents = findViewById<ImageView>(R.id.goodmorning_2_grandparents)
        val goodnight_1_grandparents = findViewById<ImageView>(R.id.goodnight_1_grandparents)
        val goodnight_2_grandparents = findViewById<ImageView>(R.id.goodnight_2_grandparents)
        val welcomehome_1_grandparents = findViewById<ImageView>(R.id.welcomehome_1_grandparents)
        val welcomehome_2_grandparents = findViewById<ImageView>(R.id.welcomehome_2_grandparents)
        val notification_unibo = findViewById<ImageView>(R.id.notification_unibo)
        val normal_face = findViewById<ImageView>(R.id.normal_face)
        val parents_face = findViewById<ImageView>(R.id.parents_face)
        val grandparents_face = findViewById<ImageView>(R.id.grandparents_face)
        val heart = findViewById<ImageView>(R.id.heart)
        val puff = findViewById<ImageView>(R.id.puff)
        val dance_left_parents = findViewById<ImageView>(R.id.dance_left_parents)
        val dance_right_parents = findViewById<ImageView>(R.id.dance_right_parents)
        val dance_left_grandparents = findViewById<ImageView>(R.id.dance_left_grandparents)
        val dance_right_grandparents = findViewById<ImageView>(R.id.dance_right_grandparents)
        val timeline_button = findViewById<ImageButton>(R.id.timeline_button)
        val mic_button = findViewById<ImageButton>(R.id.mic_button)
        val unibo_button = findViewById<ImageButton>(R.id.unibo_button)

        eye_animation = Runnable {
            if(flag) {
                normal_face.visibility = View.INVISIBLE
                flag = false
            }
            else {
                normal_face.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(eye_animation, 1000)
        }

        heart_animation = Runnable {
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            unibo_2.visibility = View.VISIBLE
            GlobalScope.launch(Dispatchers.Main) {
                var job = launch {
                    delay(800)
                }
                job.join()
                unibo_2.visibility = View.INVISIBLE
                unibo_button.visibility = View.VISIBLE
                unibo_button.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.a2))
                GlobalScope.launch(Dispatchers.Main) {
                    var job = launch {
                        delay(1000)
                    job.join()
                        heart.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.a1))
                        mic_button.isClickable = true
                        unibo_button.isClickable = true
                        timeline_button.isClickable = true
                        handler.post(eye_animation)
                    }
                }
            }
        }

        puff_animation = Runnable {
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            unibo_2.visibility = View.VISIBLE
            GlobalScope.launch(Dispatchers.Main) {
                var job = launch {
                    delay(800)
                }
                job.join()
                unibo_2.visibility = View.INVISIBLE
                unibo_button.visibility = View.VISIBLE
                unibo_button.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.a2))
                GlobalScope.launch(Dispatchers.Main) {
                    var job = launch {
                        delay(1000)
                    }
                    job.join()
                    puff.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.a1))
                    mic_button.isClickable = true
                    unibo_button.isClickable = true
                    timeline_button.isClickable = true
                    handler.post(eye_animation)
                }
            }
        }

        dance_animation_parents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                dance_left_parents.visibility = View.VISIBLE
                dance_right_parents.visibility = View.INVISIBLE
                flag = false
            }
            else {
                dance_left_parents.visibility = View.INVISIBLE
                dance_right_parents.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(dance_animation_parents, 2000)
        }

        dance_animation_grandparents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                dance_left_grandparents.visibility = View.VISIBLE
                dance_right_grandparents.visibility = View.INVISIBLE
                flag = false
            }
            else {
                dance_left_grandparents.visibility = View.INVISIBLE
                dance_right_grandparents.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(dance_animation_grandparents, 2000)
        }

        greeting_animation1_parents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                goodmorning_1_parents.visibility = View.VISIBLE
                goodmorning_2_parents.visibility = View.INVISIBLE
                flag = false
            }
            else {
                goodmorning_1_parents.visibility = View.INVISIBLE
                goodmorning_2_parents.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(greeting_animation1_parents, 3000)
        }

        greeting_animation2_parents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                goodnight_1_parents.visibility = View.VISIBLE
                goodnight_2_parents.visibility = View.INVISIBLE
                flag = false
            }
            else {
                goodnight_1_parents.visibility = View.INVISIBLE
                goodnight_2_parents.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(greeting_animation2_parents, 3000)
        }

        greeting_animation3_parents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                welcomehome_1_parents.visibility = View.VISIBLE
                welcomehome_2_parents.visibility = View.INVISIBLE
                flag = false
            }
            else {
                welcomehome_1_parents.visibility = View.INVISIBLE
                welcomehome_2_parents.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(greeting_animation3_parents, 3000)
        }

        greeting_animation1_grandparents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                goodmorning_1_grandparents.visibility = View.VISIBLE
                goodmorning_2_grandparents.visibility = View.INVISIBLE
                flag = false
            }
            else {
                goodmorning_1_grandparents.visibility = View.INVISIBLE
                goodmorning_2_grandparents.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(greeting_animation1_grandparents, 3000)
        }

        greeting_animation2_grandparents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                goodnight_1_grandparents.visibility = View.VISIBLE
                goodnight_2_grandparents.visibility = View.INVISIBLE
                flag = false
            }
            else {
                goodnight_1_grandparents.visibility = View.INVISIBLE
                goodnight_2_grandparents.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(greeting_animation2_grandparents, 3000)
        }

        greeting_animation3_grandparents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                welcomehome_1_grandparents.visibility = View.VISIBLE
                welcomehome_2_grandparents.visibility = View.INVISIBLE
                flag = false
            }
            else {
                welcomehome_1_grandparents.visibility = View.INVISIBLE
                welcomehome_2_grandparents.visibility = View.VISIBLE
                flag = true
            }
            handler.postDelayed(greeting_animation3_grandparents, 3000)
        }

        notification_parents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            parents_face.visibility = View.VISIBLE
            if(flag) {
                notification_unibo.visibility = View.INVISIBLE
                unibo_button.visibility = View.VISIBLE
                flag = false
            }
            else {
                notification_unibo.visibility = View.VISIBLE
                unibo_button.visibility = View.INVISIBLE
                flag = true
            }
            handler.postDelayed(notification_parents, 1000)
        }

        notification_grandparents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            grandparents_face.visibility = View.VISIBLE
            if(flag) {
                notification_unibo.visibility = View.INVISIBLE
                unibo_button.visibility = View.VISIBLE
                flag = false
            }
            else {
                notification_unibo.visibility = View.VISIBLE
                unibo_button.visibility = View.INVISIBLE
                flag = true
            }
            handler.postDelayed(notification_parents, 1000)
        }

        handler.post(eye_animation)

        mic_button.setOnClickListener {
            mic_button.isClickable = false
            unibo_button.isClickable = false
            timeline_button.isClickable = false
            handler.postDelayed(puff_animation,1000)
        }

        unibo_button.setOnClickListener {
            mic_button.isClickable = false
            unibo_button.isClickable = false
            timeline_button.isClickable = false
            handler.postDelayed(heart_animation,1000)
        }

        timeline_button.setOnClickListener{
            handler.removeCallbacks(eye_animation)
            mic_button.isClickable = true
            unibo_button.isClickable = true
            unibo_button.visibility = View.VISIBLE
            parents_face.visibility = View.INVISIBLE
            grandparents_face.visibility = View.INVISIBLE
            notification_unibo.visibility = View.INVISIBLE
            goodmorning_1_parents.visibility = View.INVISIBLE
            goodmorning_2_parents.visibility = View.INVISIBLE
            goodnight_1_parents.visibility = View.INVISIBLE
            goodnight_2_parents.visibility = View.INVISIBLE
            welcomehome_1_parents.visibility = View.INVISIBLE
            welcomehome_2_parents.visibility = View.INVISIBLE
            goodmorning_1_grandparents.visibility = View.INVISIBLE
            goodmorning_2_grandparents.visibility = View.INVISIBLE
            goodnight_1_grandparents.visibility = View.INVISIBLE
            goodnight_2_grandparents.visibility = View.INVISIBLE
            welcomehome_1_grandparents.visibility = View.INVISIBLE
            welcomehome_2_grandparents.visibility = View.INVISIBLE
            dance_left_parents.visibility = View.INVISIBLE
            dance_left_grandparents.visibility = View.INVISIBLE
            dance_right_parents.visibility = View.INVISIBLE
            dance_right_grandparents.visibility = View.INVISIBLE
            handler.post(eye_animation)
            handler.removeCallbacks(notification_parents)
            handler.removeCallbacks(notification_grandparents)
            handler.removeCallbacks(greeting_animation1_parents)
            handler.removeCallbacks(greeting_animation2_parents)
            handler.removeCallbacks(greeting_animation3_parents)
            handler.removeCallbacks(greeting_animation1_grandparents)
            handler.removeCallbacks(greeting_animation2_grandparents)
            handler.removeCallbacks(greeting_animation3_grandparents)
            handler.removeCallbacks(dance_animation_parents)
            handler.removeCallbacks(dance_animation_grandparents)
        }
    }
}
