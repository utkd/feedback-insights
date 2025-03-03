from typing import List
import numpy as np
from openai import OpenAI

class OpenAILLM():
    def __init__(self, client: OpenAI, model : str = 'gpt-4o-mini'):
        self._model = model
        self._client = client

    def call(self, messages: dict[str, str]) -> dict[str, str]:
        response = None
        if messages is not None and len(messages) > 0:
            response = self._client.chat.completions.create(
                messages = messages,
                model = self._model
            )
            return response.choices[0].message.content
        return response
    

class OpenAIEmbedding():
    def __init__(self, client: OpenAI, model : str = 'text-embedding-3-small'):
        self._model = model
        self._client = client

    def get_embeddings(self, input_docs: List[str]) -> np.ndarray:
        response = self._client.embeddings.create(
            input=input_docs, 
            model=self._model
        )
        embeddings = [np.array(x.embedding) for x in response.data]
        return embeddings
