# 2025-10-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.79109  |       1.11305  |   0.098829 |
| solution-pl        |     0.935696 |       0.157644 |   0.241467 |
| solution-aron-mark |     0.936871 |       0.15302  |   0.242989 |
| solution-1-flask   |     0.941918 |       1.0082   |   0.260148 |
| solution-1         |     8.64856  |       1e-06    |   0.954378 |
| solution-2         |     5.27199  |       1.00608  |   1.33498  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.493467 |       0.15735  |   0.367747 |
| solution-pl        |     0.48206  |       0.155591 |   0.368116 |
| solution-flask     |     0.48457  |       1.00838  |   0.378916 |
| solution-1-flask   |     0.491544 |       1.00837  |   0.791988 |
| solution-2         |     0.72769  |       0.504284 |   4.53098  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479467 |       0.163882 |    1.08557 |
| solution-aron-mark |     0.48259  |       0.163143 |    1.10243 |
| solution-flask     |     0.484171 |       1.00844  |    1.56445 |
| solution-1-flask   |     0.492525 |       1.00849  |    5.65584 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.489941 |       0.197055 |    3.28529 |
| solution-aron-mark |     0.483816 |       0.196942 |    3.28633 |
| solution-flask     |     0.483088 |       1.00833  |    5.11346 |