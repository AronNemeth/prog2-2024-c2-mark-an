# 2024-03-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8018   |       1.05713  |   0.065077 |
| solution-aron-mark |     0.6785   |       0.109241 |   0.162584 |
| solution-pl        |     0.654074 |       0.108739 |   0.164046 |
| solution-1-flask   |     0.66975  |       1.00816  |   0.267414 |
| solution-1         |     8.34632  |       1e-06    |   0.721322 |
| solution-2         |     4.72057  |       0.479923 |   1.14391  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660029 |       1.00848  |   0.173082 |
| solution-pl        |     0.657134 |       0.113722 |   0.252852 |
| solution-aron-mark |     0.653328 |       0.113925 |   0.265525 |
| solution-1-flask   |     0.670717 |       1.0086   |   0.790712 |
| solution-2         |     0.659818 |       0.443231 |   2.69621  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.655185 |       0.12006  |   0.806222 |
| solution-aron-mark |     0.662425 |       0.120718 |   0.807532 |
| solution-flask     |     0.659273 |       1.00846  |   0.928174 |
| solution-1-flask   |     0.669139 |       1.00872  |   5.38783  |
| solution-2         |     0.65942  |       0.503206 |  55.9994   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.658531 |       0.159549 |    3.28555 |
| solution-aron-mark |     0.66489  |       0.155364 |    3.30256 |
| solution-flask     |     0.657268 |       1.00838  |    5.4993  |