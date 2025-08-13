<h2>Prototype: ffmpeg + whisper + deep_translator local integration script</h2>
Chunk, transcribe and translate with this free local-driven intuitive python automation script. Imports OpenAIs local open source <i>whisper</i> models to transcribe and post a .srt (subtitle file). Then procceeds to translate with Google Translate deep_translator module (currently configured for pt).


---

How to use
Place this script in the same folder as your video or update VIDEO_FILE with full path.

Make sure ffmpeg is in your PATH and Whisper CLI works.

Activate your Python virtual environment with googletrans installed.

Run:

```bash
python main.py
After processing, you’ll get:
subtitles/video.srt
```

---

To-do list:
[] Easy setup for language selection
[] Optional keep video chunks for cuts integration (Easy YT Shorts, Tiktok, etc)
[] Import method for identifying chunk cut positions of interest instead of fixed timing.
[] Add UI instead of manual script file configuration.