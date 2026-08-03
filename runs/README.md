# 2026-08-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.06843  |       1.00908  |   0.097149 |
| solution-1-flask   |     1.07598  |       1.09044  |   0.221527 |
| solution-pl        |     0.4258   |       0.153586 |   0.227403 |
| solution-aron-mark |     0.438945 |       0.15309  |   0.229106 |
| solution-1         |     8.08536  |       1e-06    |   0.549703 |
| solution-2         |     4.55536  |       0.544096 |   1.21877  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.426312 |       0.153054 |   0.351323 |
| solution-pl        |     0.42784  |       0.152459 |   0.353159 |
| solution-flask     |     0.430381 |       1.00892  |   0.390522 |
| solution-1-flask   |     0.431829 |       1.009    |   0.720488 |
| solution-2         |     0.444592 |       0.494631 |   2.2847   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.420773 |       0.158312 |    1.03159 |
| solution-pl        |     0.424683 |       0.160959 |    1.03293 |
| solution-flask     |     0.419795 |       1.00892  |    1.63738 |
| solution-1-flask   |     0.459759 |       1.00933  |    5.7777  |
| solution-2         |     0.421634 |       0.552218 |   33.3728  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424341 |       0.183122 |    3.4095  |
| solution-pl        |     0.424594 |       0.182444 |    3.43014 |
| solution-flask     |     0.425084 |       1.00901  |    5.07323 |