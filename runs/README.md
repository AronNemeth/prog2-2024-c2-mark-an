# 2026-05-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.13311  |       1.13643  |   0.113678 |
| solution-pl        |     0.43291  |       0.146608 |   0.238446 |
| solution-aron-mark |     6.13678  |       0.173637 |   0.239678 |
| solution-1-flask   |     0.431314 |       1.00802  |   0.271148 |
| solution-1         |     7.67242  |       1e-06    |   0.645704 |
| solution-2         |     0.425201 |       0.634077 |   0.905308 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.428028 |       0.147268 |   0.379568 |
| solution-aron-mark |     0.450131 |       0.148612 |   0.380729 |
| solution-flask     |     0.425463 |       1.00818  |   0.411511 |
| solution-1-flask   |     0.43942  |       1.00837  |   0.801422 |
| solution-2         |     0.426899 |       0.51119  |   3.95005  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427424 |       0.154452 |    1.17372 |
| solution-aron-mark |     0.436872 |       0.15588  |    1.17946 |
| solution-flask     |     0.432815 |       1.00838  |    1.75554 |
| solution-1-flask   |     0.4405   |       1.0086   |    5.70811 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.428929 |       0.189624 |    4.01914 |
| solution-aron-mark |     0.434809 |       0.178503 |    4.0563  |
| solution-flask     |     0.431224 |       1.00842  |    5.49974 |