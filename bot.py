from pydub import AudioSegment
import speech_recognition as sr

def main():
    r = sr.Recognizer()  # подключение распознавателя

    sr.LANGUAGE = 'ru-RU' # установка языка

    # Путь к исходному .mp3 файлу на Диске

    # Путь для сохранения результата в формате .flac
    flac_file = "Bottest.flac"

    # Загрузка MP3 файла с помощью pydub
    audio = AudioSegment.from_mp3("Bottest2.mp3")

    # Экспорт аудио в формате FLAC
    audio.export(flac_file, format="flac")
    print(f"Конвертация завершена: {flac_file}")


    
    with sr.AudioFile(flac_file) as source:  # открытие аудиофайла
        audio = r.record(source)  # чтение содержимого аудиофайла

    try:
    # Распознавание речи в аудиофайле
        text = r.recognize_google(audio, language='ru-RU')
        print(f"Вы сказали: {text}")
    except sr.UnknownValueError:
        print("Не удалось распознать речь")

if __name__ == "__main__":
    main()