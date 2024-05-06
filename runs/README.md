# 2024-05-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.682439 |       1.00897  |   0.079713 |
| solution-pl        |     6.21797  |       0.121912 |   0.177603 |
| solution-aron-mark |     0.696709 |       0.119415 |   0.183125 |
| solution-1-flask   |     1.34712  |       1.08555  |   0.265397 |
| solution-1         |     7.90135  |       1e-06    |   0.584831 |
| solution-2         |     0.666104 |       0.430681 |   0.921371 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.690078 |       1.00905  |   0.17018  |
| solution-aron-mark |     0.669323 |       0.128953 |   0.276958 |
| solution-pl        |     0.682868 |       0.127304 |   0.283909 |
| solution-1-flask   |     0.701693 |       1.00915  |   0.802637 |
| solution-2         |     0.696779 |       0.463411 |   2.57049  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.70641  |       1.00954  |   0.731296 |
| solution-aron-mark |     0.69516  |       0.134706 |   0.832093 |
| solution-pl        |     0.678689 |       0.142377 |   0.853133 |
| solution-1-flask   |     0.689012 |       1.00905  |   5.63433  |
| solution-2         |     0.674925 |       0.497605 | 163.405    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674396 |       1.00916  |    2.63819 |
| solution-pl        |     0.67713  |       0.169557 |    2.75306 |
| solution-aron-mark |     0.686503 |       0.172706 |    2.78774 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.675284 |       0.304458 |    17.8518 |
| solution-flask     |     0.665067 |       1.00966  |    18.8931 |
| solution-aron-mark |     0.712057 |       0.303439 |    19.8505 |