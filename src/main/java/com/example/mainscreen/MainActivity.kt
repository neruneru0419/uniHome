package com.example.mainscreen

import android.os.Bundle
import android.os.Handler
import android.support.v7.app.AppCompatActivity
import android.view.View
import android.view.animation.AnimationUtils
import android.widget.ImageButton
import android.widget.ImageView
import com.example.mainscreen.R.layout.activity_main
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import android.app.Activity
import android.content.ActivityNotFoundException
import android.content.Intent
import android.content.pm.PackageManager
import android.speech.RecognizerIntent
import android.support.v4.app.ActivityCompat
import android.support.v4.content.ContextCompat
import android.widget.Button
import android.widget.TextView
import java.util.*

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
    var permissionState = false
    private var textView: TextView? = null
    private var lang: Int = 0

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
        val dance1_1_parents = findViewById<ImageView>(R.id.dance1_1_parents)
        val dance1_2_parents = findViewById<ImageView>(R.id.dance1_2_parents)
        val dance2_1_parents = findViewById<ImageView>(R.id.dance2_1_parents)
        val dance2_2_parents = findViewById<ImageView>(R.id.dance2_2_parents)
        val dance1_1_grandparents = findViewById<ImageView>(R.id.dance1_1_grandparents)
        val dance1_2_grandparents = findViewById<ImageView>(R.id.dance1_2_grandparents)
        val dance2_1_grandparents = findViewById<ImageView>(R.id.dance2_1_grandparents)
        val dance2_2_grandparents = findViewById<ImageView>(R.id.dance2_2_grandparents)
        val timeline_button = findViewById<ImageButton>(R.id.timeline_button)
        val mic_button = findViewById<ImageButton>(R.id.mic_button)
        val unibo_button = findViewById<ImageButton>(R.id.unibo_button)
        val recordAudioPermission = android.Manifest.permission.RECORD_AUDIO
        val currentPermissionState = ContextCompat.checkSelfPermission(this, recordAudioPermission)

        if (currentPermissionState != PackageManager.PERMISSION_GRANTED) {
            if (ActivityCompat.shouldShowRequestPermissionRationale(this, recordAudioPermission)) {
                // 拒否した場合
                permissionState = false
            } else {
                // 許可した場合
                ActivityCompat.requestPermissions(this, arrayOf(recordAudioPermission), 1)
                permissionState = true
            }
        }
        // 言語選択 0:日本語、1:英語、2:オフライン、その他:General
        lang = 0
        mic_button.setOnClickListener {
            // 音声認識を開始
            speech()
        }

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
                dance1_1_parents.visibility = View.VISIBLE
                dance2_2_parents.visibility = View.INVISIBLE
                GlobalScope.launch(Dispatchers.Main) {
                    var job = launch {
                        delay(500)
                    }
                    job.join()
                    dance1_1_parents.visibility = View.INVISIBLE
                    dance1_2_parents.visibility = View.VISIBLE
                    flag = false
                }
            }
            else{
                dance2_1_parents.visibility = View.VISIBLE
                dance1_2_parents.visibility = View.INVISIBLE
                GlobalScope.launch(Dispatchers.Main) {
                    var job = launch {
                        delay(500)
                    }
                    job.join()
                    dance2_1_parents.visibility = View.INVISIBLE
                    dance2_2_parents.visibility = View.VISIBLE
                    flag = true
                }
            }
            handler.postDelayed(dance_animation_parents, 1000)
        }

        dance_animation_grandparents = Runnable{
            handler.removeCallbacks(eye_animation)
            normal_face.visibility = View.INVISIBLE
            unibo_button.visibility = View.INVISIBLE
            if(flag) {
                dance1_1_grandparents.visibility = View.VISIBLE
                dance2_2_grandparents.visibility = View.INVISIBLE
                GlobalScope.launch(Dispatchers.Main) {
                    var job = launch {
                        delay(500)
                    }
                    job.join()
                    dance1_1_grandparents.visibility = View.INVISIBLE
                    dance1_2_grandparents.visibility = View.VISIBLE
                    flag = false
                }
            }
            else{
                dance2_1_grandparents.visibility = View.VISIBLE
                dance1_2_grandparents.visibility = View.INVISIBLE
                GlobalScope.launch(Dispatchers.Main) {
                    var job = launch {
                        delay(500)
                    }
                    job.join()
                    dance2_1_grandparents.visibility = View.INVISIBLE
                    dance2_2_grandparents.visibility = View.VISIBLE
                    flag = true
                }
            }
            handler.postDelayed(dance_animation_grandparents, 1000)
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
            handler.postDelayed(greeting_animation1_parents, 1000)
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
            handler.postDelayed(greeting_animation2_parents, 1000)
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
            handler.postDelayed(greeting_animation3_parents, 1000)
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
            handler.postDelayed(greeting_animation1_grandparents, 1000)
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
            handler.postDelayed(greeting_animation2_grandparents, 1000)
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
            handler.postDelayed(greeting_animation3_grandparents, 1000)
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
            dance1_1_parents.visibility = View.INVISIBLE
            dance1_2_parents.visibility = View.INVISIBLE
            dance2_1_parents.visibility = View.INVISIBLE
            dance2_2_parents.visibility = View.INVISIBLE
            dance1_1_grandparents.visibility = View.INVISIBLE
            dance1_2_grandparents.visibility = View.INVISIBLE
            dance2_1_grandparents.visibility = View.INVISIBLE
            dance2_2_grandparents.visibility = View.INVISIBLE
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
    private fun speech() {
        // 音声認識の　Intent インスタンス
        val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)

        if (lang == 0) {
            // 日本語
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.JAPAN.toString())
        } else if (lang == 1) {
            // 英語
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.ENGLISH.toString())
        } else if (lang == 2) {
            // Off line mode
            intent.putExtra(RecognizerIntent.EXTRA_PREFER_OFFLINE, true)
        } else {
            intent.putExtra(
                RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
            )
        }

        intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 100)
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "音声を入力")

        try {
            // インテント発行
            startActivityForResult(intent, REQUEST_CODE)
        } catch (e: ActivityNotFoundException) {
            e.printStackTrace()

        }

    }

    // 結果を受け取るために onActivityResult を設置
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (requestCode == REQUEST_CODE && resultCode == Activity.RESULT_OK) {
            // 認識結果を ArrayList で取得
            val candidates = data!!.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS)

            if (candidates.size > 0) {
                if(candidates[0] == "こんにちは"){
                    handler.postDelayed(puff_animation,1000)
                }
            }
        }
    }

    companion object {

        private val REQUEST_CODE = 1000
    }
}
