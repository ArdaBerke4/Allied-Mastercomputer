# memory/history_manager.py

import json
import os

class HistoryManager:
    def __init__(self, message_limit=20):
        # Hafıza limitini biraz artırdık ki uzun monologları daha iyi hatırlasın
        self.message_limit = message_limit
        self.log_file = "memory/am_logs.json"
        self.conversation_history = []
        self.load_history()

    def load_history(self):
        # Eğer daha önceden kaydedilmiş bir hafıza dosyası varsa onu okur
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as file:
                self.conversation_history = json.load(file)

    def save_history(self):
        # Listeyi fiziksel olarak diske yazar
        with open(self.log_file, "w", encoding="utf-8") as file:
            json.dump(self.conversation_history, file, ensure_ascii=False, indent=4)

    def add_message(self, role, content):
        # Yeni mesajı listeye ekler
        message_node = {"role": role, "content": content}
        self.conversation_history.append(message_node)
        
        # Basit bir while döngüsü ile limit kontrolü yapıyoruz
        while len(self.conversation_history) > self.message_limit:
            self.conversation_history.pop(0)
            
        # Her yeni mesaj eklendiğinde dosyayı günceller
        self.save_history()

    def get_history(self):
        return self.conversation_history