# 2024-06-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.44079  |       1.04938  |   0.076961 |
| solution-aron-mark |     5.87464  |       0.102265 |   0.160541 |
| solution-pl        |     0.665617 |       0.103057 |   0.163811 |
| solution-1-flask   |     0.688177 |       1.00917  |   0.26243  |
| solution-1         |     8.04979  |       1e-06    |   0.62845  |
| solution-2         |     0.669077 |       0.427045 |   0.674963 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664194 |       1.00949  |   0.164898 |
| solution-aron-mark |     0.691475 |       0.105888 |   0.258612 |
| solution-pl        |     0.675895 |       0.105355 |   0.270931 |
| solution-1-flask   |     0.692159 |       1.00885  |   0.789358 |
| solution-2         |     0.673247 |       0.441909 |   4.28273  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.679344 |       1.00912  |   0.720585 |
| solution-aron-mark |     0.664695 |       0.114098 |   0.831805 |
| solution-pl        |     0.673486 |       0.112583 |   0.834234 |
| solution-1-flask   |     0.682224 |       1.00884  |   5.61286  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668099 |       1.0096   |    2.53532 |
| solution-pl        |     0.677685 |       0.151092 |    2.64388 |
| solution-aron-mark |     0.686573 |       0.15149  |    2.68055 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665451 |       1.00909  |    15.694  |
| solution-aron-mark |     0.67358  |       0.28504  |    22.6533 |
| solution-pl        |     0.675483 |       0.280218 |    22.6676 |