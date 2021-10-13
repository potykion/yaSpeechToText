# yaSpeechToText

Переводит речь в текст, используя Yandex Speech Kit (YSK)

## Сетап

0. `poetry install` + создать `.env` по аналогии с `.env.sample`
1. Закинуть в `/data/acc/` или в `/data/opus/` аудио-файлы (YSK поддерживает только .opus, .acc умею переводить в .opus) 
2. Запускается это все в `acc_to_text.ipynb`
3. Там нужно прописать `/data/aac/postman.aac` в `aac_files` или для .opus файлов в `opus_files` (ну там коммент есть о этом)
4. Ну и все: по шагам выполняем ячейки, в конце результат появится в txt-файл в `data/txt/`
