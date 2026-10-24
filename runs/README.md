# 2026-10-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.20649  |       1.06332  |   0.094292 |
| solution-1-flask   |     0.305364 |       1.00767  |   0.12837  |
| solution-pl        |     0.28797  |       0.114313 |   0.152393 |
| solution-aron-mark |     4.60547  |       0.121218 |   0.154264 |
| solution-1         |     5.53401  |       0        |   0.381223 |
| solution-2         |     0.281497 |       0.550914 |   0.583489 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.319622 |       1.00783  |   0.104744 |
| solution-pl        |     0.324101 |       0.123168 |   0.228911 |
| solution-aron-mark |     0.288937 |       0.138527 |   0.258899 |
| solution-1-flask   |     0.292863 |       1.0073   |   0.389522 |
| solution-2         |     0.306553 |       0.38512  |   2.27459  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.293379 |       1.00754  |   0.488521 |
| solution-aron-mark |     0.288704 |       0.118412 |   0.563798 |
| solution-pl        |     0.297107 |       0.126996 |   0.589609 |
| solution-1-flask   |     0.292193 |       1.00727  |   2.95921  |
| solution-2         |     0.28371  |       0.403013 |  16.6146   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.280392 |       0.138382 |    1.9762  |
| solution-aron-mark |     0.290132 |       0.135234 |    1.99842 |
| solution-flask     |     0.296148 |       1.00755  |    2.35017 |
| solution-1-flask   |     0.298587 |       1.00767  |   26.6701  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.300636 |       0.207831 |    14.639  |
| solution-pl        |     0.324023 |       0.192474 |    15.1594 |
| solution-flask     |     0.306601 |       1.00743  |    17.2401 |