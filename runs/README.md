# 2026-02-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.94868  |       1.0502   |   0.098752 |
| solution-pl        |     0.390463 |       0.149301 |   0.220668 |
| solution-aron-mark |     0.409007 |       0.150199 |   0.22804  |
| solution-1-flask   |     0.400109 |       1.0063   |   0.232828 |
| solution-1         |     6.8446   |       1e-06    |   0.55074  |
| solution-2         |     4.96963  |       0.501118 |   0.92598  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.392657 |       0.15164  |   0.336667 |
| solution-aron-mark |     0.409172 |       0.156112 |   0.341279 |
| solution-flask     |     0.396569 |       1.00661  |   0.417403 |
| solution-1-flask   |     0.406459 |       1.00643  |   0.709374 |
| solution-2         |     0.389117 |       0.475071 |   2.55928  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.395004 |       0.157411 |   0.978734 |
| solution-aron-mark |     0.398868 |       0.162209 |   0.990076 |
| solution-flask     |     0.408635 |       1.00656  |   1.72998  |
| solution-1-flask   |     0.40028  |       1.00681  |   5.33144  |
| solution-2         |     0.392319 |       0.515742 | 171.692    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.395554 |       0.185583 |    4.54067 |
| solution-pl        |     0.400675 |       0.193632 |    4.68484 |
| solution-flask     |     0.394237 |       1.00636  |    5.57214 |