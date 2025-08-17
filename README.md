<h1>Prototype: ffmpeg + whisper + deep_translator local integration script</h1>
<p>Chunk, transcribe and translate with this free local-driven intuitive python automation script. Imports OpenAIs local open source whisper models to transcribe and post a .srt (subtitle file). Then procceeds to translate with Google Translate deep_translator module (currently configured for pt).</p>

---

<h2>📦 Installation</h2>

<h3>1. Install Python</h3>
<p>Make sure you have <strong>Python 3.8+</strong> installed.<br>
<a href="https://www.python.org/downloads/">Download Python</a> or install via your system package manager.</p>

<h3>2. Install FFmpeg</h3>
<p>This script requires <strong>FFmpeg</strong> installed and set to your environment PATH for video/audio processing:</p>
<h4>Windows</h4>
<ul>
<li>Download FFmpeg from <a href="https://ffmpeg.org/download.html">ffmpeg.org/download</a>.</li>
<li>Extract it to a folder (e.g., <code>C:\ffmpeg</code>).</li>
<li>Add the <code>bin</code> folder to your <strong>PATH</strong>: <code>C:\ffmpeg\bin</code></li>
</ul>
<h4>macOS</h4>
<pre><code>brew install ffmpeg
</code></pre>
<h4>Linux (Debian/Ubuntu)</h4>
<pre><code>sudo apt update && sudo apt install ffmpeg
</code></pre>

<p>To confirm FFmpeg is installed:</p>
<pre><code>ffmpeg -version
</code></pre>

<h3>3. Install Whisper CLI</h3>
<p>This script uses <a href="https://github.com/openai/whisper">OpenAI Whisper</a> for speech-to-text.</p>

<pre><code>pip install -U openai-whisper
</code></pre>

<p>Whisper requires <strong>PyTorch</strong>. If it’s not already installed, run:</p>
<pre><code>pip install torch
</code></pre>
<p><em>(For GPU acceleration, see the <a href="https://pytorch.org/get-started/locally/">PyTorch install guide</a>.)</em></p>

<p>Verify Whisper works:</p>
<pre><code>whisper --help
</code></pre>

<hr>

<h2>Run 💬</h2>
<ol>
<li>Update the path to VIDEO_FILE inside <code>main.py</code></li>
<li>Run:</li>
</ol>
<pre><code>python main.py
</code></pre>
<ol start="3">
<li>After processing, you’ll get:</li>
</ol>
<pre><code>subtitles/video.srt
</code></pre>

<hr>

<h2>🛠 To-Do List</h2>
<ul>
<li>[ ] Easy setup for language selection</li>
<li>[ ] Optional keep video chunks for cuts integration (Easy YT Shorts, TikTok, etc.)</li>
<li>[ ] Import method for identifying chunk cut positions of interest instead of fixed timing</li>
<li>[ ] Add UI instead of manual script file configuration</li>
</ul>
