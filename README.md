<!-- MAIN TITLE -->
# → LinuxBoi

<!-- LINUX BOI PICTURE -->
  <img align="right" src="https://i.imgur.com/aiIXeCJ.png" width=30%>

<!-- BADGES -->
  ![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8-blue?style=flat-square)
  ![Discord.py Version](https://img.shields.io/badge/discord.py-1.5.0-blue?style=flat-square)
  ![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square)
  ![Uptime - Current Time](https://img.shields.io/uptimerobot/status/m783893443-c045a2d525b791caafd2dcdb?style=flat-square)
  <a href="https://app.codacy.com/manual/TrackRunny/Discord-Selfbot/dashboard?bid=14423857&token=vnDn11JbhCP7nhu">![Code Quality](https://img.shields.io/codacy/grade/179a29ed15bb40b5b0eed2b695791f94?style=flat-square)</a>  

<!-- KEY INFORMATION HEADER -->
## ➤ Important Information

  * Official GitHub repo for LinuxBoi.
  * Multi-use Discord bot that is being actively developed.
  * Main purpose is to teach / help people about Linux on Discord.
  * 2 - 3 Commits each week.
  * Uptime badge to show if the bot is online or not.

<!-- MODULES HEADER -->
### ➤ Modules

  * Events  
  * Fun
  * Information
  * Linuxinfo (coming soon)
  * Meme
  * Moderation
  * Music ([Lavalink.py](https://github.com/Devoxin/Lavalink.py "Lavalink.py") for good sound quality)
  * Owner
  * Utility

<!-- INSTALLATION HEADER -->
### ➤ Installation

  **Please note that I would rather you not run another instance of the bot and just invite it to your server. If you really want to run it with your own token for testing or another reason, please follow the directions below to run it.**

  Also note that **MAC OS X CANNOT\*** run [**Lavalink Server**](https://github.com/Frederikam/Lavalink "Lavalink Server") due to a missing library that is required to run it. You can attempt to run [**Lavalink Server**](https://github.com/Frederikam/Lavalink "Lavalink Server")  on it, but when you try to play sound nothing will come out. You should get an error like this: `java.lang.UnsatisfiedLinkError: Required library at /natives/darwin/libudpqueue.dylib was not found`. Currently [**Lavalink Server**](https://github.com/Frederikam/Lavalink "Lavalink Server")  supports Windows and Linux.
  [**Lavalink.py**](https://github.com/Devoxin/Lavalink "Lavalink.py") does support Mac OS X, however this is a wrapper for Lavalink server. Lavalink server allows you to play sound with the bot.

  \* Its not impossible to try and compile Lavalink.jar with Mac natives up and running, though it has been done before but I personally have never tried it.

---

  <!-- Installation Instructions -->
  There is a requirements.txt file that anyone on **Any Operating That Supports Python 3.6+** can use to install **All** of the dependencies needed for LinuxBoi to run. If your computer / server has two versions of **python and / or you have python 2 and python 3 installed make sure to use python 3.6+**. Installation instructions are below as follows:

  * First, clone this repo and install the dependencies from the txt file.

  ```markdown
  git clone https://github.com/TrackRunny/LinuxBoi.git

  cd LinuxBoi

  pip install --user --requirement requirements.txt
  <!-- Remember: Only use this if you only have python 3 installed. -->

  or

  pip3 install --user --requirement requirements.txt
  <!-- Remember: Use this if you have two versions of python and / or you have python 2 and python 3. -->  
  ```

  <!-- Windows Microsoft Visual C++ 14.0 Error -->
  * If your using windows, please read this portion below.

  <details>
    <summary><b>Click here</b></summary>
    <h3>➤ Error: Microsoft Visual C++ 14.0 is required.</h3>
    <p>Note, some users may receive this error above when trying to install the dependencies from the requirements.txt file. This happens when you are trying to build and install the <b>Pycosat</b> pip module. If this happens to you, please follow the instructions below.</p>
  
  1. Download the compiled **Pycosat** file for your Python version and windows architecture.
      * [**Pycosat | Python 3.7 | Win32**](https://mega.nz/#!4BVgjYhI!1EqFNPdbPUGRImfs3GSaWQLe9u3ClVRjzm8NJEMWmMs)
      * [**Pycosat | Python 3.7 | Win64**](https://mega.nz/#!RdVkFSIT!ZHoTnlkTtIPJQYv-8W7vxCfBZKTmuyw2Rgst6ea10Lo)
      * [**Pycosat | Python 3.8 | Win32**](https://mega.nz/file/lVVjjY5a#hOJqA9eOeRBP1KRxpImHHwK4dZ-rm1oY-HJmnm7WrzU)
      * [**Pycosat | Python 3.8 | Win64**](https://mega.nz/file/oJMT3IQK#bYJzvYyKN0B0zhuOpMINu9THMRu7e9H-447b6edX-2w)
  2. Change directories into the downloaded file.
  3. Install the compiled pip module.

  ```markdown
    pip install pycosat-0.6.3-cp37-cp37m-win32.whl
    <!-- Win32 | Python 3.7 -->

    pip install pycosat-0.6.3-cp37-cp37m-win_amd64.whl
    <!-- Win64 | Python 3.7 -->
    
    ---
    
    pip install pycosat-0.6.3-cp38-cp38-win32.whl
    <!-- Win32 | Python 3.8 -->

    pip install pycosat-0.6.3-cp38-cp38-win_amd64.whl
    <!-- Win64 | Python 3.8 -->

    or

    pip3 install pycosat-0.6.3-cp37-cp37m-win32.whl
    <!-- Win32 | Python 3.7 | pip3 -->

    pip3 install pycosat-0.6.3-cp37-cp37m-win_amd64.whl
    <!-- Win64 | Python 3.7 | pip3 -->

    ---

    pip3 install pycosat-0.6.3-cp38-cp38-win32.whl
    <!-- Win32 | Python 3.8 | pip3 -->

    pip3 install pycosat-0.6.3-cp38-cp38-win_amd64.whl
    <!-- Win64 | Python 3.8 | pip3-->
  ```

  </details>

<!-- Installation with Environment Variables-->
### ➤ Environment Variables (Continuing Installation)

  There are some environment variables you need to have on the computer / server that is running the Discord bot. **If you don't have these the bot will not work correctly!**

  I have created a copy and paste area for all the environment variables that you need for the bot. The instructions are below depending on which operating system you use.

  <details>
    <summary><b>Linux</b> (Click the arrow)</summary>
    <h3>➤ Environment Variables On Linux</h3>
    <p>Linux: Put the variables at the end of your <b>.bashrc</b> file. The <b>.bashrc</b> file is located in your home directory. You can copy and paste these and put in the values. These are located under the Windows instructions inside the code block.</p>
    <p>Here is an example of what it should look like.</p>
    <img src="https://i.imgur.com/KEzwZdW.png">
  </details>

  <details>
    <summary><b>Mac OS X</b> (Click the arrow)</summary>
    <h3>➤ Environment Variables On Mac</h3>
    <p>Mac OS X: Put the variables at the end of your <b>.bash_profile</b> file. The <b>.bash_profile</b> is located in your home directory. You can copy and paste these and put in the values. These are located under the Windows instructions inside the code block.</p>
    <p>Here is an example of what it should look like.</p>
    <img src="https://i.imgur.com/KEzwZdW.png">
  </details>

  <details>
    <summary><b>Windows</b> (Click the arrow)</summary>
    <h3>➤ Environment Variables On Windows</h3>
    <p>Windows: The process is a little more difficult on Windows. Please watch <a href="https://www.youtube.com/watch?v=IolxqkL7cD8">this</a> video so you can export these values on your Windows Operating System. Skip to <b>1:19</b> if you want to see how he does it. Make sure to keep the enviroment variables with the same name or they won't work. The variable names are inside the code block just under this piece of text.</p>
  </details>
  
  ```bash
  export ip_info=""
  export email=""
  export email_password=""
  export bitly_access_token=""
  export weather_key=""
  export ksoft_key=""
  export top_gg_key=""
  export linuxboi_token=""
  export linuxboi_testing_token=""
  ```

### ➤ List of Api's (Continuing Installation)

  These are all of the api's I use inside LinuxBoi.

  1. [**Ip Info**](https://ipinfo.io/) (Free; Sign up to receive an api key)

  2. [**Bitly**](https://dev.bitly.com/) (Free; Sign up to receive a generic access token)

  3. [**Open Weather API**](https://openweathermap.org/api) (Free; Sign up the receive an api key)
  
  4. [**KSoft.Si API**](https://api.ksoft.si/) (Free; Sign up to receive an api token)
  
  5. [**TopGG API**](https://top.gg) (Free; Sign up to receive an api token)

  6. [**Gmail**](https://gmail.com/) (Free; Sign up, use account email and password)

  You need to put these values inside the environment variables. You also need to provide a bot token for the linuxboi_token, and linuxboi_testing_token enviroment variables too.

### ➤ Finishing Installation

  Congrats, everything should be set up correctly so far. If you want to start the bot you can do `./LinuxBoi.py` as it should already be executable.

  Don't forget to start Lavalink server too! To do this you can change directories into `cd Music/`. After that you can do `java -jar Lavalink.jar`. **Note:** You need to have Java 11 or higher to run this correctly. I would **recommend** starting **Lavalink server before starting the bot** as you won't get the `[NODE-us-127.0.0.1:2333] Failed to establish connection!` error when you start the bot before Lavalink server is running.

---

<!-- LICENSE INFO -->
## ➤ License

  This project is licensed under the GPLv3.

<!-- END OF README -->
## ➤ Questions / Contact me

  * Discord Account: `TrackRunny#0001`
