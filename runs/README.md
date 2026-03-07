# 2026-03-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.15056  |       1.0438   |   0.112334 |
| solution-aron-mark |     0.444679 |       0.146477 |   0.236252 |
| solution-pl        |     4.71875  |       0.14773  |   0.238049 |
| solution-1-flask   |     0.455748 |       1.00855  |   0.266021 |
| solution-1         |     8.01004  |       1e-06    |   0.657071 |
| solution-2         |     0.441794 |       0.598938 |   1.0795   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.44759  |       0.148165 |   0.373744 |
| solution-pl        |     0.455074 |       0.147695 |   0.380617 |
| solution-flask     |     0.444911 |       1.00886  |   0.404739 |
| solution-1-flask   |     0.451057 |       1.00879  |   0.860059 |
| solution-2         |     0.44383  |       0.510489 |   4.57959  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.474535 |       0.154176 |    1.15728 |
| solution-aron-mark |     0.448221 |       0.159996 |    1.16846 |
| solution-flask     |     0.446683 |       1.00884  |    1.64502 |
| solution-1-flask   |     0.451609 |       1.00883  |    5.63117 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.445333 |       0.181487 |    3.89232 |
| solution-aron-mark |     0.449307 |       0.185229 |    3.98692 |
| solution-flask     |     0.443814 |       1.00882  |    5.25677 |