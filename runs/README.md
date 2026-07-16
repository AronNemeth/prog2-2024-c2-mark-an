# 2026-07-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.52844  |       1.20167  |   0.121285 |
| solution-pl        |     0.494269 |       0.150901 |   0.236054 |
| solution-aron-mark |     0.920789 |       0.149903 |   0.241231 |
| solution-1-flask   |     0.924255 |       1.00854  |   0.273766 |
| solution-1         |     8.19987  |       1e-06    |   0.67127  |
| solution-2         |     5.22189  |       0.698265 |   1.2054   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430202 |       0.153333 |   0.374729 |
| solution-aron-mark |     0.43302  |       0.151351 |   0.379873 |
| solution-flask     |     0.438195 |       1.00892  |   0.409858 |
| solution-1-flask   |     0.436857 |       1.00858  |   0.816242 |
| solution-2         |     0.429589 |       0.519412 |  12.2451   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429927 |       0.157795 |    1.14269 |
| solution-aron-mark |     0.431915 |       0.15897  |    1.14989 |
| solution-flask     |     0.435623 |       1.00887  |    1.74505 |
| solution-1-flask   |     0.44798  |       1.00878  |    5.80754 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.437231 |       0.186242 |    4.12721 |
| solution-pl        |     0.425946 |       0.183059 |    4.12812 |
| solution-flask     |     0.428106 |       1.00869  |    5.47269 |