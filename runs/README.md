# 2026-02-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.65352  |       1.06013  |   0.105523 |
| solution-pl        |     0.445198 |       0.144809 |   0.231024 |
| solution-aron-mark |     0.447211 |       0.148041 |   0.23447  |
| solution-1-flask   |     0.446313 |       1.0083   |   0.267311 |
| solution-1         |     7.81997  |       1e-06    |   0.714325 |
| solution-2         |     4.76904  |       0.671731 |   1.09937  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.439382 |       0.146186 |   0.355794 |
| solution-aron-mark |     0.440483 |       0.14904  |   0.35697  |
| solution-flask     |     0.45075  |       1.00849  |   0.43503  |
| solution-1-flask   |     0.444474 |       1.00856  |   0.801507 |
| solution-2         |     0.442163 |       0.506977 |   2.78733  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.439414 |       0.154377 |    1.08559 |
| solution-pl        |     0.451797 |       0.153753 |    1.08987 |
| solution-flask     |     0.444064 |       1.00846  |    1.58569 |
| solution-1-flask   |     0.450892 |       1.0085   |    5.62346 |
| solution-2         |     0.437407 |       0.565804 |   28.2403  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.446519 |        0.18017 |    3.80426 |
| solution-aron-mark |     0.452021 |        0.18136 |    3.82794 |
| solution-flask     |     0.445733 |        1.00883 |    5.16613 |