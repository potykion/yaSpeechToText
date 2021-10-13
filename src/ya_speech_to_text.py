import os

import requests


class YaSpeechToTextCli(requests.Session):
    API_KEY = os.environ["YA_SPEECH_KIT_API_KEY"]
    SECRET = os.environ["YA_SPEECH_KIT_SECRET"]

    def __init__(self):
        super().__init__()
        self.headers["Authorization"] = F"Api-Key {YaSpeechToTextCli.SECRET}"

    def start_recognize_audio(self, audio_cdn_url):
        resp = self.post(
            "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize",
            json={
                "config": {
                    "specification": {
                        "languageCode": "ru-RU",
                        "model": "general",
                        "profanityFilter": False,
                        "audioEncoding": "OGG_OPUS",
                    }
                },
                "audio": {
                    "uri": audio_cdn_url
                }
            }
        )
        return resp.json()

    def get_recognize_status(self, id_or_res):
        id_ = id_or_res if isinstance(id_or_res, str) else id_or_res["id"]
        resp = self.get(f"https://operation.api.cloud.yandex.net/operations/{id_}")
        return resp.json()


def merge_parsed_text(parse_res: dict):
    return "\n".join([chunk["alternatives"][0]["text"] for chunk in parse_res["response"]["chunks"]])
