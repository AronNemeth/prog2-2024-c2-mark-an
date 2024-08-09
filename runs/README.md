# 2024-08-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.563031 |       1.00937  |   0.078115 |
| solution-aron-mark |     1.84872  |       0.10711  |   0.171394 |
| solution-pl        |     0.571147 |       0.103778 |   0.171756 |
| solution-1-flask   |     1.10131  |       1.10194  |   0.264147 |
| solution-1         |     7.68389  |       1e-06    |   0.613697 |
| solution-2         |     4.3968   |       0.590407 |   0.859285 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.566437 |       1.00935  |   0.225538 |
| solution-aron-mark |     0.583091 |       0.103959 |   0.289703 |
| solution-pl        |     0.577353 |       0.104976 |   0.29232  |
| solution-1-flask   |     0.577237 |       1.009    |   0.780043 |
| solution-2         |     0.571909 |       0.481706 |   3.32486  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.574315 |       1.0094   |   0.928966 |
| solution-aron-mark |     0.574679 |       0.113889 |   0.990515 |
| solution-pl        |     0.564283 |       0.113938 |   1.03042  |
| solution-1-flask   |     0.584925 |       1.00945  |   5.64889  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.591322 |       0.144971 |    4.44464 |
| solution-aron-mark |     0.577797 |       0.146115 |    4.46915 |
| solution-flask     |     0.572981 |       1.00936  |    4.61468 |