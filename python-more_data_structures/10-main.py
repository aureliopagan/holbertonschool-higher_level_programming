def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)

# Example usage
if __name__ == "__main__":
    scores = {
        'Alice': 90,
        'Bob': 85,
        'Charlie': 95
    }
    print("Best score:", best_score(scores))