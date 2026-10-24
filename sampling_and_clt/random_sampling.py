
import numpy as np

def take_random_sample(data, sample_size, replace=True, random_state=None):
    data = np.asarray(data)

    if data.size == 0:
        raise ValueError("data cannot be empty")
    if not 1 <= sample_size <= data.size and not replace:
        raise ValueError("invalid sample_size without replacement")
    if sample_size < 1:
        raise ValueError("sample_size must be positive")

    rng = np.random.default_rng(random_state)

    return rng.choice(data, size=sample_size, replace=replace)

data = np.array([10, 20, 30, 40, 50, 60, 70, 80])

sample = take_random_sample(
    data,
    sample_size=4,
    replace=False,
    random_state=42
)

print("Random sample:", sample)
