# 2024-05-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.693165 |       1.0094   |   0.074578 |
| solution-pl        |     5.9512   |       0.126485 |   0.177807 |
| solution-aron-mark |     0.706247 |       0.123641 |   0.178287 |
| solution-1-flask   |     1.35306  |       1.1034   |   0.267834 |
| solution-1         |     8.10564  |       1e-06    |   0.602931 |
| solution-2         |     0.68621  |       0.433547 |   1.66163  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.689257 |       1.0092   |   0.169845 |
| solution-aron-mark |     0.701574 |       0.129942 |   0.276155 |
| solution-pl        |     0.686465 |       0.129613 |   0.276648 |
| solution-1-flask   |     0.698669 |       1.00908  |   0.80961  |
| solution-2         |     0.688508 |       0.446953 |   4.54461  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.690333 |       1.00926  |   0.707134 |
| solution-aron-mark |     0.681981 |       0.137943 |   0.822691 |
| solution-pl        |     0.679588 |       0.136348 |   0.823142 |
| solution-1-flask   |     0.701055 |       1.00952  |   5.71048  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.680773 |       1.00892  |    2.55848 |
| solution-aron-mark |     0.685729 |       0.172467 |    2.71647 |
| solution-pl        |     0.691972 |       0.173317 |    2.71748 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.699574 |       0.30675  |    16.9941 |
| solution-flask     |     0.696491 |       1.00948  |    17.4162 |
| solution-pl        |     0.686934 |       0.302773 |    17.5972 |