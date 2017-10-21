# coordstring

A fast container for geospatial coordinates.

## Usage

```python
from coordstring import CoordString

coordinates = CoordString([(0, 10), (2, 8), (3, 5), (2, 4)])

position = coordinates[0]
subset = coordinates.slice(0, -1, 2)
bbox = coordinates.bbox()
```

## Benchmarks

| Initialization    | Time      |
|-------------------|-----------|
| python            | 4.26      |
| numpy             | 3.61      |
| CoordString       | 0.842     |

| Indexing          | Time      |
|-------------------|-----------|
| python            | 0.421     |
| numpy             | 1.72      |
| CoordString       | 0.727     |

| Slicing           | Time      |
|-------------------|-----------|
| python            | 0.920     |
| numpy             | 0.217     |
| CoordString       | 0.708     |

| Bounding box      | Time      |
|-------------------|-----------|
| python            | 14.8      |
| numpy             | 0.243     |
| CoordString       | 0.137     |

