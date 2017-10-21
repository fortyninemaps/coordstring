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
| numpy             | 3.61      |
| CoordString       | 0.842     |

| Indexing          | Time      |
|-------------------|-----------|
| python            | 0.421     |
| numpy             | 1.72      |
| CoordString       | 1.04      |

| Slicing           | Time      |
|-------------------|-----------|
| python            | 0.938     |
| numpy             | 0.239     |
| CoordString       | 0.782     |

| Bounding box      | Time      |
|-------------------|-----------|
| python            | 2.94      |
| numpy             | 0.0508    |
| CoordString       | 0.0275    |

