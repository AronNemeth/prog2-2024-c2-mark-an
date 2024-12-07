# 2024-12-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.10501  |       1.10476  |   0.104275 |
| solution-aron-mark |     0.552212 |       0.107342 |   0.176312 |
| solution-pl        |     5.63043  |       0.108797 |   0.177386 |
| solution-1-flask   |     0.573611 |       1.00903  |   0.252747 |
| solution-1         |     7.44674  |       1e-06    |   0.578602 |
| solution-2         |     0.548835 |       0.502213 |   1.3617   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.560749 |       0.10965  |   0.295495 |
| solution-pl        |     0.559713 |       0.109244 |   0.296215 |
| solution-flask     |     0.557639 |       1.00935  |   0.500676 |
| solution-1-flask   |     0.566851 |       1.00887  |   0.745375 |
| solution-2         |     0.55776  |       0.472219 |  21.1211   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.557431 |       0.117301 |    1.02435 |
| solution-pl        |     0.558416 |       0.116571 |    1.02592 |
| solution-flask     |     0.558349 |       1.01179  |    2.22227 |
| solution-1-flask   |     0.560797 |       1.00909  |    5.38005 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.566767 |       0.14664  |    4.26931 |
| solution-aron-mark |     0.557969 |       0.146079 |    4.31085 |
| solution-flask     |     0.556306 |       1.00892  |    8.63019 |