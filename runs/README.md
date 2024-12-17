# 2024-12-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.2216   |       1.00866  |   0.103158 |
| solution-aron-mark |     0.52682  |       0.105934 |   0.184182 |
| solution-pl        |     0.528945 |       0.108024 |   0.184741 |
| solution-1-flask   |     5.25595  |       1.1674   |   0.264506 |
| solution-1         |     8.03016  |       1e-06    |   0.822688 |
| solution-2         |     0.533975 |       0.551464 |   1.51398  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534535 |       0.108442 |   0.313734 |
| solution-aron-mark |     0.53239  |       0.109308 |   0.318217 |
| solution-flask     |     0.52956  |       1.00912  |   0.536603 |
| solution-1-flask   |     0.535684 |       1.00882  |   0.806471 |
| solution-2         |     0.531022 |       0.477695 |   5.51441  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.540207 |       0.11643  |    1.07214 |
| solution-pl        |     0.527275 |       0.116541 |    1.08029 |
| solution-flask     |     0.528676 |       1.0088   |    2.27772 |
| solution-1-flask   |     0.53502  |       1.00906  |    5.89349 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.527408 |       0.141736 |    4.43254 |
| solution-aron-mark |     0.525349 |       0.14659  |    4.49439 |
| solution-flask     |     0.530825 |       1.01038  |    8.91622 |