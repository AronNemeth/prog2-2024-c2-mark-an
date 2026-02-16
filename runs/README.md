# 2026-02-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.55545  |       1.08527  |   0.108832 |
| solution-pl        |     4.4805   |       0.146094 |   0.230331 |
| solution-aron-mark |     0.44447  |       0.145624 |   0.235849 |
| solution-1-flask   |     0.458477 |       1.00876  |   0.262583 |
| solution-1         |     7.39925  |       1e-06    |   0.734891 |
| solution-2         |     0.444559 |       0.734218 |   1.12903  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.44956  |       0.147859 |   0.367948 |
| solution-pl        |     0.450317 |       0.147883 |   0.368495 |
| solution-flask     |     0.445381 |       1.00879  |   0.391292 |
| solution-1-flask   |     0.450699 |       1.00901  |   0.783651 |
| solution-2         |     0.448027 |       0.510139 |   3.04578  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.450361 |       0.155287 |    1.12185 |
| solution-aron-mark |     0.448979 |       0.154746 |    1.14135 |
| solution-flask     |     0.445907 |       1.00883  |    1.64909 |
| solution-1-flask   |     0.447293 |       1.00916  |    5.53554 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.450587 |       0.179535 |    3.86638 |
| solution-aron-mark |     0.447647 |       0.183238 |    3.9318  |
| solution-flask     |     0.440889 |       1.00906  |    5.18197 |