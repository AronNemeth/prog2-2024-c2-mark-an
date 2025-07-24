# 2025-07-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.44377  |       1.07844  |   0.104633 |
| solution-pl        |     0.496397 |       0.151405 |   0.237097 |
| solution-aron-mark |     4.56104  |       0.148233 |   0.237896 |
| solution-1-flask   |     0.507898 |       1.00836  |   0.266026 |
| solution-1         |     7.67493  |       1e-06    |   1.00017  |
| solution-2         |     0.496255 |       0.887315 |   1.05008  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.501918 |       0.150869 |   0.363728 |
| solution-pl        |     0.501861 |       0.152216 |   0.367009 |
| solution-flask     |     0.498049 |       1.00824  |   0.389271 |
| solution-1-flask   |     0.528246 |       1.00858  |   0.795301 |
| solution-2         |     0.500675 |       0.515072 |   2.91542  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.533473 |       0.15868  |    1.07777 |
| solution-pl        |     0.521041 |       0.164313 |    1.08807 |
| solution-flask     |     0.512295 |       1.00864  |    1.58038 |
| solution-1-flask   |     0.522785 |       1.00856  |    5.72118 |
| solution-2         |     0.508743 |       0.559913 |  179.731   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.510641 |       0.187999 |    3.27334 |
| solution-aron-mark |     0.508437 |       0.190686 |    3.31325 |
| solution-flask     |     0.523551 |       1.00854  |    5.29021 |