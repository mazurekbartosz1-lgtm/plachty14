"""
Rekompresuje wszystkie filmy w videos/ z lepszymi ustawieniami (mniejszy rozmiar).
CRF 30, preset medium -> ~40-60% mniejsze niż CRF 28 + fast.
Konwertuje w miejscu: najpierw do temp pliku, potem nadpisuje oryginał.
"""
import subprocess, os

FFMPEG = r"C:\Users\Julia\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe"
VID_DIR = r"C:\Projekty\Plachty14\videos"

videos = [f for f in os.listdir(VID_DIR) if f.lower().endswith('.mp4')]
print(f"Znaleziono {len(videos)} filmow\n")

total_before = 0
total_after = 0

for name in sorted(videos):
    src = os.path.join(VID_DIR, name)
    tmp = src + '.tmp.mp4'

    orig_mb = os.path.getsize(src) / 1024 / 1024
    total_before += orig_mb

    cmd = [
        FFMPEG, '-y', '-i', src,
        '-vf', 'scale=1280:-2',
        '-c:v', 'libx264', '-crf', '30', '-preset', 'medium',
        '-c:a', 'aac', '-b:a', '96k',
        '-movflags', '+faststart',
        tmp
    ]
    print(f"Kompresuję: {name} ({orig_mb:.1f} MB)...")
    result = subprocess.run(cmd, capture_output=True)

    if result.returncode == 0:
        new_mb = os.path.getsize(tmp) / 1024 / 1024
        total_after += new_mb
        os.replace(tmp, src)
        saved = orig_mb - new_mb
        print(f"  OK: {orig_mb:.1f} MB -> {new_mb:.1f} MB  (zaoszczedzono {saved:.1f} MB, {saved/orig_mb*100:.0f}%)")
    else:
        if os.path.exists(tmp):
            os.remove(tmp)
        print(f"  BLAD: {result.stderr[-300:].decode(errors='ignore')}")

print(f"\nPodsumowanie:")
print(f"  Przed: {total_before:.1f} MB")
print(f"  Po:    {total_after:.1f} MB")
print(f"  Zaoszczedzono: {total_before - total_after:.1f} MB ({(total_before - total_after)/total_before*100:.0f}%)")
