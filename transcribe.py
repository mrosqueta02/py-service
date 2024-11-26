import whisper
import os

output = 'outFiles'

if not os.path.exists(output):
    os.makedirs(output)

model = whisper.load_model('small')

def transcribe(file_name):
    print(f'starting {file_name}')
    
    result = model.transcribe(file_name, language='tl')

    text = result['text']
    
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    
    out_file = os.path.join(output, f'{base_name}.txt')
    
    # write the text to the output text file
    with open(out_file, mode='w') as file:
        file.write(text)

    # print the text to the console
    print(f'finished {file_name}')