# py_youtube_downloader
Download all videos from a Youtube play list.

This based on youtube_dl.

Run the app:

python start.py "ListId" "youremailaccount@gmail.com" "yourPassword" "DestinationDirectory" "saveFormat"
 
    * keep the password simple. Some special characters will cause errors.
   
    * for the url https://www.youtube.com/playlist?list=PLoRCKRqklUyWv6m1fB_WcuL5dKgLqgoxA
      the listid is                                     PLoRCKRqklUyWv6m1fB_WcuL5dKgLqgoxA

    * do not end the DestinationDirectory with a slash \. This is the escape character. It will add " to you path.

    * saveFormat is "mp3" or "mp4". Watch caps.

Required Libraries

    * pip install youtube_dl
        (Note this library updates frequently, so your app might break. Application should check for new updates and install them before running.)
    * pip install pandas

Required Additional Tools/Apps

    * ffmpeg: https://www.ffmpeg.org/download.html