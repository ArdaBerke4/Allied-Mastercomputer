# knowledge/vector_store.py

import ollama

class VectorStore:
    def __init__(self):
        self.document_chunks = []
        self.chunk_embeddings = []
        self.embedding_model = "nomic-embed-text"

    def add_chunk(self, chunk_text):
        # Metni modele gönderip sayısal vektör dizisini alıyoruz
        response = ollama.embeddings(model=self.embedding_model, prompt=chunk_text)
        vector_data = response["embedding"]
        
        self.document_chunks.append(chunk_text)
        self.chunk_embeddings.append(vector_data)

    def find_best_match(self, user_query):
        if len(self.document_chunks) == 0:
            return ""

        # Kullanıcının sorusunu da aynı şekilde vektöre çeviriyoruz
        response = ollama.embeddings(model=self.embedding_model, prompt=user_query)
        query_vector = response["embedding"]

        best_score = -1.0
        best_chunk = ""
        
        # Sadece temel for döngüleri kullanarak saf matematiksel benzerlik hesabı
        for i in range(len(self.chunk_embeddings)):
            current_vector = self.chunk_embeddings[i]
            
            dot_product = 0.0
            norm_a = 0.0
            norm_b = 0.0
            
            for j in range(len(query_vector)):
                dot_product += query_vector[j] * current_vector[j]
                norm_a += query_vector[j] * query_vector[j]
                norm_b += current_vector[j] * current_vector[j]
            
            # Sıfıra bölünme hatasını engelleme
            if norm_a == 0.0 or norm_b == 0.0:
                similarity = 0.0
            else:
                similarity = dot_product / ((norm_a ** 0.5) * (norm_b ** 0.5))
            
            if similarity > best_score:
                best_score = similarity
                best_chunk = self.document_chunks[i]
                
        return best_chunk