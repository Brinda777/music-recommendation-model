def mean_average_precision(recommended_lists, relevant_lists):
    average_precisions = []

    for recommended, relevant in zip(recommended_lists, relevant_lists):
        num_hits = 0
        precision_sum = 0

        for i, song in enumerate(recommended):
            if song in relevant:
                num_hits += 1
                precision_at_i = num_hits / (i + 1)
                precision_sum += precision_at_i

        average_precision = precision_sum / len(relevant) if relevant else 0
        average_precisions.append(average_precision)

    return sum(average_precisions) / len(average_precisions) if average_precisions else 0
