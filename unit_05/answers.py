def get_class_average(class_scores: dict) -> float:
    """ Returns the average score of the class. """
    total: float = 0.0
    count: int = 0
    # You can use .values() to get all the scores
    for score in class_scores.values():
        total += score
        count += 1
    # Or you can iterate through the dictionary directly
    # for student in class_scores:
    #     total += class_scores[student]
    #     count += 1
    return total / count if count > 0 else 0.0

def get_class_median(class_scores: dict) -> float:
    """ """
    # We're not worried about the names, just the scores
    scores: list = list(class_scores.values())
    # Sort the scores
    scores.sort()
    # Using the modulus operator to see if the length of the list is odd or even
    if len(scores) % 2 == 1:
        # Odd length - return the middle value
        median_index: int = len(scores) // 2
        return scores[median_index]
    else:
        # Even length - return the average of the two middle values
        mid_index1: int = (len(scores) // 2) - 1
        mid_index2: int = len(scores) // 2
        return (scores[mid_index1] + scores[mid_index2]) / 2
