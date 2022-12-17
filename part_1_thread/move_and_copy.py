import os
from pathlib import Path
from funk_normalize import normalize
from threading import Thread, RLock

extension_dict = {
    'images': ['jpeg', 'jpg', 'svg', 'png'],
    'video': ['avi', 'mp4', 'mov', 'mkv'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'audio': ['mp3', 'ogg', 'wav', 'amr'],
    'archives': ['zip', 'tar', 'gz'],
    'unknown': []
}

main_directory = Path('C:\\SORT_FOLDER\\')
if not os.path.isdir(main_directory):
    os.makedirs(main_directory)


def find_format(file):
    for suf in extension_dict:
        if file.name.split('.')[-1] in extension_dict[suf]:
            dir_img = main_directory / suf
            dir_img.mkdir(exist_ok=True)
            name = file.name.replace(file.name.split(
                '.')[0], normalize(file.name.split('.')[0]))
            file.replace(dir_img.joinpath(name))
            return True
    return False


lock = RLock()


def sort_folder(path, locker = lock):
    folder = Path(path)
    for file in folder.iterdir():
        if file.is_dir():
            if file.name in ('audio', 'video', 'documents', 'images', 'archives', 'unknown'):
                continue
            t1 = Thread(target=sort_folder, args=(file, lock))
            t1.start()
            t1.join()
            if not os.listdir(file):
                os.rmdir(file)
        else:
            if not find_format(file):
                dir_unk = main_directory / 'unknown'
                dir_unk.mkdir(exist_ok=True)
                name = file.name.replace(file.name.split(
                    '.')[0], normalize(file.name.split('.')[0]))
                file.replace(dir_unk.joinpath(name))




sort_folder('C:\\Projects\\web_3\\TEMP')

