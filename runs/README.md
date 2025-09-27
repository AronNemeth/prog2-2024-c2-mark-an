# 2025-09-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.32307  |       1.05011  |   0.100696 |
| solution-pl        |     0.487752 |       0.155654 |   0.237472 |
| solution-aron-mark |     0.487827 |       0.150863 |   0.237719 |
| solution-1-flask   |     0.48703  |       1.00825  |   0.267543 |
| solution-1         |     7.9493   |       1e-06    |   0.726    |
| solution-2         |     4.4244   |       0.723519 |   1.43689  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.490266 |       0.156079 |   0.365113 |
| solution-pl        |     0.491854 |       0.158443 |   0.366865 |
| solution-flask     |     0.486204 |       1.00845  |   0.378233 |
| solution-1-flask   |     0.496279 |       1.00842  |   0.811705 |
| solution-2         |     0.487303 |       0.514392 |   3.33919  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.502325 |       0.16256  |    1.07446 |
| solution-pl        |     0.495902 |       0.162448 |    1.07824 |
| solution-flask     |     0.486748 |       1.00849  |    1.5861  |
| solution-1-flask   |     0.489051 |       1.00874  |    5.7284  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.491813 |       0.193285 |    3.28791 |
| solution-pl        |     0.496961 |       0.191889 |    3.30091 |
| solution-flask     |     0.488609 |       1.00967  |    5.21852 |