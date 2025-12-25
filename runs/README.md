# 2025-12-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.40716  |       1.05726  |   0.087456 |
| solution-aron-mark |     0.421475 |       0.149364 |   0.213634 |
| solution-pl        |     0.427604 |       0.146919 |   0.214849 |
| solution-1-flask   |     0.424196 |       1.00665  |   0.227474 |
| solution-1         |     6.3121   |       1e-06    |   0.618242 |
| solution-2         |     3.95907  |       0.648609 |   1.293    |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.424361 |       0.148903 |   0.324141 |
| solution-aron-mark |     0.421268 |       0.148768 |   0.326424 |
| solution-flask     |     0.420743 |       1.00675  |   0.403977 |
| solution-1-flask   |     0.425552 |       1.00655  |   0.712325 |
| solution-2         |     0.418561 |       0.473793 |   4.01433  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.419634 |       0.153625 |   0.980358 |
| solution-pl        |     0.420546 |       0.155945 |   0.984744 |
| solution-flask     |     0.420678 |       1.0069   |   1.7471   |
| solution-1-flask   |     0.42597  |       1.00677  |   5.37448  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.418988 |       0.179552 |    3.93948 |
| solution-aron-mark |     0.42074  |       0.179893 |    4.00399 |
| solution-flask     |     0.417337 |       1.00663  |    5.59377 |