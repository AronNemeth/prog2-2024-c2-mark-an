# 2025-02-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548681 |       1.00876  |   0.083834 |
| solution-aron-mark |     0.551608 |       0.145713 |   0.207008 |
| solution-pl        |     1.75286  |       0.151519 |   0.208413 |
| solution-1-flask   |     5.13625  |       1.08148  |   0.27335  |
| solution-1         |     7.71725  |       1e-06    |   0.618313 |
| solution-2         |     0.549161 |       0.546484 |   0.908599 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.543179 |       1.00899  |   0.292013 |
| solution-aron-mark |     0.546914 |       0.145039 |   0.303281 |
| solution-pl        |     0.549281 |       0.1441   |   0.308285 |
| solution-1-flask   |     0.552063 |       1.00904  |   0.789787 |
| solution-2         |     0.558171 |       0.516156 |  11.6822   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.549358 |       0.15968  |   0.895914 |
| solution-aron-mark |     0.550929 |       0.153438 |   0.902619 |
| solution-flask     |     0.547306 |       1.00909  |   1.24805  |
| solution-1-flask   |     0.552284 |       1.00911  |   5.69549  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.557283 |       0.183605 |    2.91902 |
| solution-pl        |     0.545808 |       0.180033 |    2.93895 |
| solution-flask     |     0.542506 |       1.009    |    4.2758  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.550269 |       0.288183 |    17.7538 |
| solution-aron-mark |     0.547323 |       0.28226  |    17.7768 |