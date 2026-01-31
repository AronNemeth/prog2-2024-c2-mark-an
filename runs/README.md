# 2026-01-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.82818  |       1.07416  |   0.099887 |
| solution-aron-mark |     0.460963 |       0.160959 |   0.241209 |
| solution-pl        |     0.469974 |       0.163092 |   0.244857 |
| solution-1-flask   |     0.471822 |       1.00821  |   0.268791 |
| solution-1         |     7.38335  |       1e-06    |   0.667001 |
| solution-2         |     4.38599  |       0.597558 |   1.11114  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.467735 |       0.164388 |   0.365897 |
| solution-pl        |     0.477087 |       0.161869 |   0.36661  |
| solution-flask     |     0.475012 |       1.00839  |   0.38067  |
| solution-1-flask   |     0.470782 |       1.00846  |   0.810058 |
| solution-2         |     0.461319 |       0.506714 |   4.17091  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476381 |       0.173483 |    1.06624 |
| solution-pl        |     0.462861 |       0.172048 |    1.0738  |
| solution-flask     |     0.472013 |       1.00855  |    1.59223 |
| solution-1-flask   |     0.482699 |       1.00832  |    5.5746  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.461584 |       0.194255 |    3.43938 |
| solution-aron-mark |     0.459903 |       0.191347 |    3.46217 |
| solution-flask     |     0.460429 |       1.00882  |    5.05261 |