def get_score_level(score):
    level_by_score_range = {(90, 100): 'A', (80, 89): 'B', (70, 79): 'C', (60, 69): 'D', (0, 59): 'F'}
    for key in level_by_score_range.keys():
        if key[0] <= score <= key[1]:
            return level_by_score_range.get(key)
    raise ValueError('Invalid parameters: score=%d' % score)

