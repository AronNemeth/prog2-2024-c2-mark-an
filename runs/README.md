# 2024-10-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.37415  |       1.10438  |   0.083231 |
| solution-aron-mark |     1.89046  |       0.100508 |   0.174217 |
| solution-pl        |     0.550306 |       0.100667 |   0.175381 |
| solution-1-flask   |     0.565551 |       1.00808  |   0.260183 |
| solution-1         |     7.7722   |       1e-06    |   0.588149 |
| solution-2         |     4.55104  |       0.517356 |   0.863456 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.552902 |       1.00808  |   0.208075 |
| solution-aron-mark |     0.554639 |       0.102637 |   0.303031 |
| solution-pl        |     0.549523 |       0.102281 |   0.305315 |
| solution-1-flask   |     0.568346 |       1.0092   |   0.76649  |
| solution-2         |     0.55685  |       0.476018 |   3.39409  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.560107 |       1.00852  |   0.924227 |
| solution-aron-mark |     0.568233 |       0.109462 |   1.03575  |
| solution-pl        |     0.561786 |       0.110689 |   1.08626  |
| solution-1-flask   |     0.56983  |       1.00857  |   5.48326  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.555308 |       1.00833  |    4.16819 |
| solution-pl        |     0.558368 |       0.138618 |    4.25354 |
| solution-aron-mark |     0.570938 |       0.13816  |    4.32012 |