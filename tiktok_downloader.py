import os
     import yt_dlp
     from datetime import datetime

     USERS = ["upminaaaa", "upminaa.cos"]
     SAVE_PATH = "videos/"

     def download_new_videos():
         os.makedirs(SAVE_PATH, exist_ok=True)
         for username in USERS:
             try:
                 ydl_opts = {
                     'extract_flat': True,
                     'playlist_items': '1',
                     'quiet': True,
                 }
                 with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                     info = ydl.extract_info(f"https://www.tiktok.com/@{username}", download=False)
                     if 'entries' in info:
                         video_url = info['entries'][0]['url']
                         video_id = video_url.split('/video/')[-1].split('?')[0]
                         if not os.path.exists(f"{SAVE_PATH}{username}_{video_id}.mp4"):
                            
                             ydl_opts_download = {
                                 'outtmpl': f"{SAVE_PATH}{username}_%(id)s.%(ext)s",
                                 'quiet': True,
                             }
                             with yt_dlp.YoutubeDL(ydl_opts_download) as ydl_download:
                                 ydl_download.download([video_url])
                             print(f"⬇️ Nuevo video de @{username} descargado")
             except Exception as e:
                 print(f"❌ Error con @{username}: {str(e)}")

     if __name__ == "__main__":
         download_new_videos()
