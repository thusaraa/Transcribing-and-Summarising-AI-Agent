from transformers import pipeline

def summarize_text(text: str, model_name="facebook/bart-large-cnn",
                   max_length=130, min_length=30) -> str:
    # Load the summarization pipeline
    summarizer = pipeline("summarization")
    
    # Generate the summary
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    
   
    summarizer = pipeline("summarization", model=model_name)

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

    return summary[0]['summary_text']