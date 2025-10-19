# 2025-10-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.48795  |       1.04962  |   0.102908 |
| solution-pl        |     4.65733  |       0.152299 |   0.237753 |
| solution-aron-mark |     0.484155 |       0.154572 |   0.254565 |
| solution-1-flask   |     0.488512 |       1.00841  |   0.262104 |
| solution-1         |     7.60925  |       1e-06    |   0.731059 |
| solution-2         |     0.486582 |       0.723406 |   1.60025  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.486482 |       0.154417 |   0.370639 |
| solution-pl        |     0.486072 |       0.159891 |   0.373389 |
| solution-flask     |     0.515399 |       1.00905  |   0.384157 |
| solution-1-flask   |     0.491463 |       1.00837  |   0.777804 |
| solution-2         |     0.485209 |       0.498322 |  12.2775   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.487612 |       0.163521 |    1.10964 |
| solution-aron-mark |     0.487241 |       0.162904 |    1.11011 |
| solution-flask     |     0.491339 |       1.00845  |    1.60819 |
| solution-1-flask   |     0.490363 |       1.00834  |    5.56807 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48492  |       0.196598 |    3.2737  |
| solution-aron-mark |     0.490211 |       0.193713 |    3.29289 |
| solution-flask     |     0.489709 |       1.00894  |    5.1024  |