# 2024-04-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.66473  |       1.00945  |   0.075037 |
| solution-aron-mark |     0.67255  |       0.113112 |   0.171989 |
| solution-pl        |     5.84904  |       0.114774 |   0.177224 |
| solution-1-flask   |     1.34407  |       1.09348  |   0.270453 |
| solution-1         |     7.97807  |       1e-06    |   0.60646  |
| solution-2         |     0.685253 |       0.446699 |   0.979447 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656308 |       1.00879  |   0.1643   |
| solution-pl        |     0.667084 |       0.120821 |   0.267006 |
| solution-aron-mark |     0.660877 |       0.118624 |   0.274408 |
| solution-1-flask   |     0.675093 |       1.00907  |   0.807036 |
| solution-2         |     0.665613 |       0.436392 |   2.40793  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662236 |       1.00923  |   0.711157 |
| solution-aron-mark |     0.674388 |       0.128395 |   0.824985 |
| solution-pl        |     0.657507 |       0.126017 |   0.848902 |
| solution-1-flask   |     0.670385 |       1.00896  |   5.56979  |
| solution-2         |     0.666053 |       0.485455 | 178.29     |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656003 |       1.009    |    2.50925 |
| solution-pl        |     0.674077 |       0.160607 |    2.63375 |
| solution-aron-mark |     0.680719 |       0.163323 |    2.67684 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662447 |       1.00935  |    15.8752 |
| solution-aron-mark |     0.657605 |       0.282066 |    15.8977 |
| solution-pl        |     0.659686 |       0.289291 |    16.2632 |