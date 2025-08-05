def calculateStats(numbers):
    if not numbers:
        return {"avg": float('nan'), "min": float('nan'), "max": float('nan')}
    return {
        "avg": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }
