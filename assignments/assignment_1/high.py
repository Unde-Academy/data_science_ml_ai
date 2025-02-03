def highest_score(scores):
    if not scores:
        return None  # Return None if the list is empty
    
    max_score = scores[0]  # Assume the first score is the highest
    
    for score in scores[1:]:  # Loop through the remaining scores
        if score > max_score:
            max_score = score  # Update max_score if a higher value is found
    
    return max_score

# Example usage
scores = [23, 45, 67, 89, 12]
print("Highest score:", highest_score(scores))  # Output: 89
