# 2024-10-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.1283   |       1.10275  |   0.095737 |
| solution-pl        |     5.66748  |       0.105045 |   0.171764 |
| solution-aron-mark |     0.562152 |       0.104185 |   0.187806 |
| solution-1-flask   |     0.571791 |       1.00926  |   0.263117 |
| solution-2         |     0.562821 |       0.642507 |   0.76913  |
| solution-1         |     7.6012   |       1e-06    |   0.802394 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.563771 |       1.00914  |   0.225128 |
| solution-aron-mark |     0.562528 |       0.104897 |   0.294661 |
| solution-pl        |     0.579557 |       0.105843 |   0.294888 |
| solution-1-flask   |     0.609568 |       1.00877  |   0.765976 |
| solution-2         |     0.565243 |       0.481157 |   3.13774  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.565825 |       1.0091   |   0.911857 |
| solution-aron-mark |     0.583461 |       0.116363 |   0.989149 |
| solution-pl        |     0.572981 |       0.115987 |   0.99789  |
| solution-1-flask   |     0.600517 |       1.0092   |   5.42116  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.568747 |       1.00923  |    4.39816 |
| solution-aron-mark |     0.566149 |       0.145411 |    4.44087 |
| solution-pl        |     0.569828 |       0.143801 |    4.45159 |