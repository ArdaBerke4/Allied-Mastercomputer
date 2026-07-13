# knowledge/document_loader.py

import os

def load_and_chunk_texts(directory_path, chunk_size=200):
    all_chunks = []
    file_list = os.listdir(directory_path)
    file_index = 0
    
    # Klasördeki dosyaları tek tek geziyoruz
    while file_index < len(file_list):
        file_name = file_list[file_index]
        
        # Sadece .txt dosyalarını işleme al
        if file_name.endswith(".txt"):
            file_path = directory_path + "/" + file_name
            
            with open(file_path, 'r', encoding='utf-8') as file:
                raw_text = file.read()
                
            words = raw_text.split()
            current_word_index = 0
            
            # Metni belirlediğimiz chunk_size (örn: 200 kelime) bloklarına ayırıyoruz
            while current_word_index < len(words):
                chunk_words = []
                j = 0
                
                while j < chunk_size and (current_word_index + j) < len(words):
                    chunk_words.append(words[current_word_index + j])
                    j += 1
                    
                chunk_text = " ".join(chunk_words)
                all_chunks.append(chunk_text)
                
                current_word_index += chunk_size
                
        file_index += 1
        
    return all_chunks