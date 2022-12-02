def combine_text(*texts):
    print("function from hacktivate")
    return "\n".join(texts)


def count_sentences(*texts):
    print("function from hacktivate")
    counts = {}
    for idx, text in enumerate(texts):
        counts[idx] = len(text)
    return counts