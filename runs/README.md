# 2026-02-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8273   |       1.09195  |   0.103957 |
| solution-pl        |     0.442579 |       0.143892 |   0.224292 |
| solution-aron-mark |     0.440557 |       0.143523 |   0.226915 |
| solution-1-flask   |     0.442999 |       1.00816  |   0.266698 |
| solution-1         |     7.90071  |       1e-06    |   0.707201 |
| solution-2         |     4.73603  |       0.646809 |   0.787665 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.440814 |       0.145351 |   0.349411 |
| solution-aron-mark |     0.443425 |       0.146532 |   0.353406 |
| solution-flask     |     0.458551 |       1.00855  |   0.375755 |
| solution-1-flask   |     0.443259 |       1.00857  |   0.786149 |
| solution-2         |     0.437217 |       0.504907 |   3.94293  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.443378 |       0.150957 |    1.05459 |
| solution-aron-mark |     0.440163 |       0.154208 |    1.08555 |
| solution-flask     |     0.437288 |       1.00833  |    1.55671 |
| solution-1-flask   |     0.447336 |       1.00839  |    5.6485  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438042 |       0.179142 |    3.61611 |
| solution-pl        |     0.437953 |       0.177062 |    3.65853 |
| solution-flask     |     0.447146 |       1.00857  |    5.02133 |