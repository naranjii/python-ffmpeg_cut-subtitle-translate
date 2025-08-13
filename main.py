import os
import subprocess
from googletrans import Translator
from pathlib import Path

# ---------------- CONFIG ---------------- #
VIDEO_FILE = "00-00--01-05.mp4"               # Your input video
CHUNK_DIR = "chunks"                          # Folder to store video chunks
SUB_DIR = "subtitles"                         # Folder to store subtitles
FINAL_SRT = "video_pt.srt"                    # Output translated subtitle
CHUNK_SECONDS = 600                           # 10 minutes per chunk
WHISPER_MODEL = "small"                       # CPU-friendly model
# ---------------------------------------- #

os.makedirs(CHUNK_DIR, exist_ok=True)
os.makedirs(SUB_DIR, exist_ok=True)

# --------- 1️⃣ Split video into chunks --------- #
print("Splitting video into chunks...")
split_cmd = [
    "ffmpeg",
    "-i", VIDEO_FILE,
    "-c", "copy",
    "-map", "0",
    "-segment_time", str(CHUNK_SECONDS),
    "-f", "segment",
    os.path.join(CHUNK_DIR, "chunk_%03d.mp4")
]
subprocess.run(split_cmd, check=True)
print("Video split complete.")

# --------- 2️⃣ Transcribe each chunk --------- #
chunk_files = sorted(Path(CHUNK_DIR).glob("chunk_*.mp4"))
translator = Translator()
all_translated_lines = []

for chunk in chunk_files:
    print(f"Transcribing {chunk.name} ...")
    subprocess.run([
        "whisper",
        str(chunk),
        "--model", WHISPER_MODEL,
        "--language", "English",
        "--task", "transcribe",
        "--output_dir", SUB_DIR,
        "--output_format", "srt"
    ], check=True)

    # Find generated .srt file
    srt_file = Path(SUB_DIR) / (chunk.stem + ".srt")
    if not srt_file.exists():
        print(f"Skipping {chunk.name}, no .srt found.")
        continue

    # --------- 3️⃣ Translate subtitles --------- #
    with open(srt_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    translated_lines = []
    for line in lines:
        line_strip = line.strip()
        # Skip timestamps and numbers
        if line_strip and not "-->" in line_strip and not line_strip.isdigit():
            translated_text = translator.translate(line_strip, src="en", dest="pt").text
            translated_lines.append(translated_text)
        else:
            translated_lines.append(line_strip)
    
    all_translated_lines.extend(translated_lines)
    all_translated_lines.append("")  # Add blank line between chunks

# --------- 4️⃣ Save final translated .srt --------- #
final_path = Path(SUB_DIR) / FINAL_SRT
with open(final_path, "w", encoding="utf-8") as f:
    f.write("\n".join(all_translated_lines))

print(f"✅ Translation complete! Final SRT saved as: {final_path}")
