# 2025-01-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.46075  |       1.14841  |   0.083357 |
| solution-aron-mark |     0.523862 |       0.135527 |   0.199707 |
| solution-pl        |     4.61569  |       0.137256 |   0.202115 |
| solution-1-flask   |     0.547786 |       1.00871  |   0.264162 |
| solution-2         |     0.524882 |       1.02469  |   0.756328 |
| solution-1         |     8.05349  |       1e-06    |   1.01019  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.528644 |       1.00889  |   0.290948 |
| solution-aron-mark |     0.541222 |       0.141913 |   0.301457 |
| solution-pl        |     0.525858 |       0.137002 |   0.301508 |
| solution-1-flask   |     0.53457  |       1.00871  |   0.811261 |
| solution-2         |     0.527284 |       0.481655 |   3.79952  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.531856 |       0.145283 |   0.893901 |
| solution-aron-mark |     0.544912 |       0.148239 |   0.902734 |
| solution-flask     |     0.531858 |       1.00875  |   1.24447  |
| solution-1-flask   |     0.534578 |       1.00899  |   5.77106  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.528903 |       0.172976 |    2.81391 |
| solution-pl        |     0.535298 |       0.174705 |    2.84241 |
| solution-flask     |     0.540018 |       1.0091   |    4.25286 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.535081 |       0.285764 |    16.7647 |
| solution-pl        |     0.527588 |       0.280473 |    16.8727 |