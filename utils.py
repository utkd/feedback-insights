import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from typing import List

def process_batch(input_feedbacks, add_idx=False):
    """
    Helper function to clean and concatenate a list of input strings for input to an LLM

    :param input_feedbacks: List of strings (or a pandas Series)
    :param add_idx: If the index of the string should be added in the input
    :return: Concantenated list of strings
    """
    llm_inputs = []
    for idx, inp in enumerate(input_feedbacks):
        x = inp.replace("\n", " ")
        x = x.replace("\s+", " ")
        if add_idx:
            llm_inputs.append(str(idx) + " - " + x)
        else:
            llm_inputs.append(x)
    llm_inputs = "\n".join(llm_inputs)
    return llm_inputs

def prep_messages(sys_prompt: str=None, message_content: str=None) -> List[dict[str:str]]:
    """
    Composes the input prompt and message content into a chat format for LLM input

    :param sys_prompt: System prompt for the LLM
    :param message_content: Message content from the user's perspective
    :return: List of messages in chat format
    """
    llm_input = []
    if sys_prompt is not None:
        llm_input.append({
            "role": "system",
            "content": sys_prompt
        })
    if message_content is not None:
        llm_input.append({
            "role": "user",
            "content": message_content
        })
    return llm_input


def clean_info_response(response_str: str) -> List[str]:
    """
    Creates a list of prediction labels from the LLM response string

    :param response_str: Output from the LLM
    :return: List of predicted labels
    """
    response_arr = response_str.split("\n")
    response_arr = [r.strip() for r in response_arr]
    return [1 if "HAS_INFO" in r else 0 for r in response_arr]


def cluster_documents_kmeans(embeddings: np.ndarray, num_clusters: int):
    """
    Clusters document embeddings using KMeans with cosine similarity.

    :param embeddings: NumPy array of shape (num_documents, embedding_dim)
    :param num_clusters: Number of clusters to form
    :return: List of cluster labels
    """
    # Normalize embeddings to ensure cosine similarity is used
    embeddings_normalized = normalize(embeddings, axis=1)

    # Apply KMeans
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(embeddings_normalized)

    return cluster_labels