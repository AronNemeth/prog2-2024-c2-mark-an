# 2024-06-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.677224 |       1.00889  |   0.076297 |
| solution-pl        |     0.665303 |       0.105255 |   0.159261 |
| solution-aron-mark |     6.31443  |       0.102679 |   0.164914 |
| solution-1-flask   |     1.33913  |       1.15575  |   0.261944 |
| solution-1         |     9.00942  |       1e-06    |   0.695876 |
| solution-2         |     0.662571 |       0.684755 |   1.17238  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.680361 |       1.00913  |   0.165441 |
| solution-pl        |     0.686344 |       0.108579 |   0.262554 |
| solution-aron-mark |     0.675297 |       0.104811 |   0.269081 |
| solution-1-flask   |     0.708979 |       1.00901  |   0.781629 |
| solution-2         |     0.682852 |       0.481298 |   4.61491  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.708325 |       1.00905  |   0.711348 |
| solution-pl        |     0.696434 |       0.116686 |   0.808935 |
| solution-aron-mark |     0.706367 |       0.115883 |   0.819945 |
| solution-1-flask   |     0.706938 |       1.00897  |   5.62387  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.685188 |       1.00882  |    2.6097  |
| solution-aron-mark |     0.683896 |       0.153404 |    2.68387 |
| solution-pl        |     0.693283 |       0.154031 |    2.71276 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.673103 |       1.00942  |    16.0201 |
| solution-pl        |     0.674515 |       0.270527 |    22.2574 |
| solution-aron-mark |     0.693949 |       0.28673  |    23.9494 |