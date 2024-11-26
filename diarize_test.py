from pathlib import Path
from pyannote.audio import Pipeline
import pyannote
import whisper
import os

def get_words_timestamps(result_transcription dict) - dict
    words = {}
    word_counter = 0
    for segment in result_transcription[segments]
        for word in segment[words]
            words[fword_{word_counter}] = {
                text word[word],
                start word[start],
                end word[end],
            }
            word_counter += 1
    return words
    
def words_per_segment(
    res_transcription dict,
    res_diarization pyannote.core.Annotation,
    add_buffer bool = False,
    fixed_margin float = 0.5,
    gap_scale_factor float = 0.3,
) - dict
    def calculate_dynamic_buffer(idx, segments)

        if idx == 0 or idx == len(segments) - 1
            return fixed_margin
        previous_end = segments[idx - 1].end
        current_start = segments[idx].start
        return (current_start - previous_end)  gap_scale_factor

    res_trans_dia = {}
    segments = list(res_diarization.itersegments())

    words = get_words_timestamps(res_transcription)

    for idx, (segment, _, speaker) in enumerate(
        res_diarization.itertracks(yield_label=True)
    )
        buffer_time = calculate_dynamic_buffer(idx, segments) if add_buffer else 0

        adjusted_start = max(0, segment.start - buffer_time) if idx != 0 else 0
        adjusted_end = (
            segment.end + buffer_time if idx != len(segments) - 1 else segment.end
        )

        segment_words = []
        for _, word in words.items()
            if word[start] = adjusted_start and word[end] = adjusted_end
                segment_words.append(word[text])
            if word[start] = adjusted_end
                break

        res_trans_dia[fsegment_{idx}] = {
            speaker speaker,
            text  .join(segment_words),
            start adjusted_start,
            end adjusted_end,
        }
    return res_trans_dia

pipeline = Pipeline.from_pretrained(
    pyannotespeaker-diarization-3.1, use_auth_token=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
)

model = whisper.load_model(small)
diarization_result = pipeline(test4.mp3)
transcription_result = model.transcribe(test4.mp3, word_timestamps=True)

final_result = words_per_segment(transcription_result, diarization_result)

for _, segment in final_result.items()
    print(f'{segment[start].3f}t{segment[end].3f}t {segment[speaker]}t{segment[text]}')
