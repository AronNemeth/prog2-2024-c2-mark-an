# 2024-08-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.58919  |       1.15907  |   0.089169 |
| solution-aron-mark |     0.813603 |       0.102588 |   0.170423 |
| solution-pl        |     2.24842  |       0.106361 |   0.172378 |
| solution-1-flask   |     0.564465 |       1.00911  |   0.263798 |
| solution-1         |     8.24202  |       1e-06    |   0.819741 |
| solution-2         |     4.91386  |       0.687304 |   0.932527 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.555981 |       1.00903  |   0.229064 |
| solution-pl        |     0.551671 |       0.104718 |   0.286959 |
| solution-aron-mark |     0.560969 |       0.105594 |   0.287162 |
| solution-1-flask   |     0.57005  |       1.0091   |   0.784026 |
| solution-2         |     0.5559   |       0.479182 |   3.29508  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.563372 |       1.00897  |   0.9173   |
| solution-aron-mark |     0.56997  |       0.115536 |   0.988167 |
| solution-pl        |     0.570754 |       0.112873 |   1.02745  |
| solution-1-flask   |     0.589263 |       1.00897  |   5.68123  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.555506 |       0.145059 |    4.08166 |
| solution-pl        |     0.565926 |       0.145145 |    4.28892 |
| solution-flask     |     0.568021 |       1.00892  |    4.36384 |