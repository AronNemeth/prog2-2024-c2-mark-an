# 2026-08-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.74029  |       1.17407  |   0.076587 |
| solution-1-flask   |     0.338384 |       1.00726  |   0.176581 |
| solution-aron-mark |     3.71026  |       0.122951 |   0.182119 |
| solution-pl        |     0.331622 |       0.127509 |   0.185812 |
| solution-1         |     6.08194  |       1e-06    |   0.496183 |
| solution-2         |     0.332222 |       0.510315 |   0.816471 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.336885 |       0.123274 |   0.281471 |
| solution-aron-mark |     0.332225 |       0.122194 |   0.281596 |
| solution-flask     |     0.335638 |       1.00808  |   0.303777 |
| solution-1-flask   |     0.339546 |       1.0074   |   0.560563 |
| solution-2         |     0.33343  |       0.405637 |   2.74203  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.342352 |       0.132651 |   0.823132 |
| solution-pl        |     0.33106  |       0.158654 |   0.873493 |
| solution-flask     |     0.330631 |       1.00743  |   1.26909  |
| solution-1-flask   |     0.33453  |       1.00843  |   4.41411  |
| solution-2         |     0.332122 |       0.444288 |  40.3744   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.335603 |       0.166047 |    2.75044 |
| solution-pl        |     0.341501 |       0.155978 |    2.80313 |
| solution-flask     |     0.333772 |       1.00737  |    4.0266  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.35104  |       0.296697 |    16.5836 |
| solution-pl        |     0.368152 |       0.269495 |    17.049  |