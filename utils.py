def chunk_text(text: str, chunk_size: int = 2000, overlap: int = 200) -> list:
    """
    Splits text into chunks of a specified size.

    Args:
        text (str): The text to be split.
        chunk_size (int): The maximum size of each chunk.

    Returns:
        list: A list of text chunks.
    """
    # Split the text into words
    words = text.split()
    
    # Create chunks
    chunks = []
    start = 0
    text_len = len(text)
    
    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunk = text[start:end]
        chunks.append(chunk)

        start += end - overlap  # Overlap the next chunk with the end of the current one

        if start < 0:
            start = 0  # Ensure start index is not negative

    return chunks


def chunked_summary(text: str, summarize_func, chunk_size: int = 2000, overlap: int = 200) -> str:
    """
    Splits text into chunks and summarizes each chunk.

    Args:
        text (str): The text to be summarized.
        summarize_func (callable): The summarization function to use.
        chunk_size (int): The maximum size of each chunk.

    Returns:
        str: The summarized text.
    """
    # Split the text into chunks
    text_chunks = chunk_text(text, chunk_size, overlap)
    
    # Summarize each chunk
    partial_summaries = [summarize_func(chunk) for chunk in text_chunks]
    
    # Combine the summaries into a single string
    combined_summary_inout = " ".join(partial_summaries)

    final_summary = summarize_func(combined_summary_inout)
    
    return final_summary