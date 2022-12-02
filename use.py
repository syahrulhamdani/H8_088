def combine_text(*texts):
    print("function from use.py")
    return "\n".join(texts)


def count_sentences(*texts):
    print("function from use.py")
    counts = {}
    for idx, text in enumerate(texts):
        counts[idx] = len(text)
    return counts