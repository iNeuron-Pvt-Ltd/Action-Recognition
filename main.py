from gluoncv.utils.filesystem import try_import_decord
from gluoncv.data.transforms import video
import numpy as np

class VideoDecord:
    def __init__(self, videoname):
        decord = try_import_decord()
        self.vr=decord.VideoReader(videoname)

    def detect(self):
        fast_frame_id_list = range(0, 64, 2)
        slow_frame_id_list = range(0, 64, 16)
        frame_id_list = list(fast_frame_id_list) + list(slow_frame_id_list)
        video_data = self.vr.get_batch(frame_id_list).asnumpy()
        clip_input = [video_data[vid, :, :, :] for vid, _ in enumerate(frame_id_list)]
        transform_fn = video.VideoGroupValTransform(size=224, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        clip_input = transform_fn(clip_input)
        clip_input = np.stack(clip_input, axis=0)
        clip_input = clip_input.reshape((-1,) + (36, 3, 224, 224))
        clip_input = np.transpose(clip_input, (0, 2, 1, 3, 4))
        print('Video data is downloaded and preprocessed.')
        return clip_input






