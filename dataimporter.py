import csv
import os
import pytube
import moviepy.editor as mp

class AudioSet:
    """Constructor for dataset"""
    def __init__(self, subset_ids: dict):
        self.subset_ids = subset_ids
        self.path_csv_train = "./datasets/AudioSet/balanced_train_segments.csv"
        self.path_csv_test = "./datasets/AudioSet/eval_segments.csv"
        self.path_output_train = "./datasets/AudioSet/train_segments/"
        self.path_output_test = "./datasets/AudioSet/test_segments/"
        pass
    
    def get_rows_relevant(self):
        with open(self.path_csv_train, "r") as data:
            reader = csv.reader(data)
            for i in range(3):
                next(reader)
            audioset_train = [row for row in reader]
        # audioset_train = [[re.sub(re.compile(r'^\W+'), '', s[0])]+s[1:] for s in audioset_train]
        audioset_train = [sublist for sublist in audioset_train if any(string in sublist for string in self.subset_ids.values())]
        with open(self.path_csv_test, "r") as data:
            reader = csv.reader(data)
            for i in range(3):
                next(reader)
            audioset_test = [row for row in reader]
        # audioset_test = [[re.sub(re.compile(r'^\W+'), '', s[0])]+s[1:] for s in audioset_test]
        audioset_test = [sublist for sublist in audioset_test if any(string in sublist for string in self.subset_ids.values())]
        return audioset_train, audioset_test
    
    def download_relevant(self, audioset: list, path_output: str):
        for item in audioset:
            video_id = item[0]
            time_start = item[1]
            time_end = item[2]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            print(video_url)
            try:
                yt = pytube.YouTube(video_url)
                audio = yt.streams.filter(only_audio=True).first()
            except (pytube.exceptions.VideoUnavailable, KeyError):
                continue
            audio_filename = audio.download()
            audio_clip = mp.AudioFileClip(audio_filename).subclip(time_start, time_end)
            try:
                audio_clip.write_audiofile(f"{path_output}{video_id}.mp3")
            except (IOError):
                pass
            audio_clip.close()
            os.remove(audio_filename)
            

subset_ids = {
            "Fly": "/m/0h2mp", 
            "Cricket": "/m/09xqv",
        }

audioset = AudioSet(subset_ids)
audioset_train, audioset_test = audioset.get_rows_relevant()
audioset.download_relevant(audioset_test, audioset.path_output_test)