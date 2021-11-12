from pydub import AudioSegment
import os
import math

class SplitConvert():
    def __init__(self,folder,filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.filename = self.filename.replace("ogg","wav")
        self.audio = AudioSegment.from_ogg(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        parts = []
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(int(i/min_per_split)) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(int(i/min_per_split)) + ' Done')
            if i == total_mins - min_per_split:
                print('All split successfully')
            parts.append(split_fn)
        return(parts)


if __name__ == '__main__':
    folder = 'C:\\Users\\Vasco\\Documents\\Python\\SchwurbelTranskipt'
    file = 'test 7min.ogg'
    split_wav = SplitConvert(folder,file)
    split_wav.multiple_split(min_per_split=5)