# coordstring

A fast container for geospatial coordinates.

## Usage

```python

coordinates = CoordString([(0, 10), (2, 8), (3, 5), (2, 4)])

position = coordinates[0]
subset = coordinates.slice(0, -1, 2)
bbox = coordinates.bbox()
```

## Benchmarks

| Initialization    | Time      |
|-------------------|-----------|
| python            | 4.26      |
| numpy             | 0.0567    |
| CoordString       | 0.0297    |

| Indexing          | Time      |
|-------------------|-----------|
| python            | 0.424     |
| numpy             | 1.75      |
| CoordString       | 0.784     |

| Slicing           | Time      |
|-------------------|-----------|
| python            | 0.969     |
| numpy             | 0.221     |
| CoordString       | 1.26      |

| Bounding box      | Time      |
|-------------------|-----------|
| python            | 3.02      |
| numpy             | 0.0495    |
| CoordString       | 0.0280    |

