from collections import Counter
import gc

types = Counter(type(obj) for obj in gc.get_objects())
print(types.most_common(10))