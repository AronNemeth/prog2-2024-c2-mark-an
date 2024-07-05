# 2024-07-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492532 |       1.00873  |   0.085746 |
| solution-pl        |     0.486259 |       0.099893 |   0.165561 |
| solution-aron-mark |     5.83319  |       0.106197 |   0.16674  |
| solution-1-flask   |     1.39742  |       1.10844  |   0.259526 |
| solution-1         |     8.2503   |       1e-06    |   0.577523 |
| solution-2         |     0.488394 |       0.492327 |   0.764003 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.488172 |       1.00888  |   0.218443 |
| solution-aron-mark |     0.494087 |       0.099999 |   0.286329 |
| solution-pl        |     0.493377 |       0.100825 |   0.288142 |
| solution-1-flask   |     0.495091 |       1.00905  |   0.764665 |
| solution-2         |     0.504952 |       0.480829 |  12.8883   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.48935  |       1.00863  |   0.891298 |
| solution-aron-mark |     0.491851 |       0.109397 |   0.986351 |
| solution-pl        |     0.506641 |       0.109199 |   0.988166 |
| solution-1-flask   |     0.49824  |       1.0088   |   5.51703  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.487418 |       1.00916  |    3.9978  |
| solution-pl        |     0.497511 |       0.145319 |    4.09015 |
| solution-aron-mark |     0.492208 |       0.144999 |    4.11552 |