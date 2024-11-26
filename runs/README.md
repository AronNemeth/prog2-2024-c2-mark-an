# 2024-11-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.13639  |       1.08814  |   0.113367 |
| solution-pl        |     5.73361  |       0.110138 |   0.182377 |
| solution-aron-mark |     0.578871 |       0.108176 |   0.190123 |
| solution-1-flask   |     0.572292 |       1.00882  |   0.266459 |
| solution-2         |     0.561853 |       0.680193 |   0.820052 |
| solution-1         |     7.54576  |       1e-06    |   0.870806 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.571406 |       0.11097  |   0.302521 |
| solution-pl        |     0.574657 |       0.110024 |   0.303706 |
| solution-flask     |     0.554589 |       1.00906  |   0.497771 |
| solution-1-flask   |     0.581352 |       1.00987  |   0.769979 |
| solution-2         |     0.565207 |       0.482923 |   2.22384  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.623565 |       0.117304 |    1.02895 |
| solution-aron-mark |     0.561818 |       0.118862 |    1.04199 |
| solution-flask     |     0.563333 |       1.00917  |    2.179   |
| solution-1-flask   |     0.569414 |       1.009    |    5.37487 |
| solution-2         |     0.562113 |       0.525312 |   43.1358  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.559909 |       0.14546  |    4.39064 |
| solution-pl        |     0.557837 |       0.149308 |    4.39728 |
| solution-flask     |     0.567053 |       1.00927  |    8.72496 |