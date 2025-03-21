# 2025-03-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.528118 |       1.00879  |   0.083127 |
| solution-aron-mark |     2.03997  |       0.126022 |   0.188569 |
| solution-pl        |     0.521023 |       0.124881 |   0.190405 |
| solution-1-flask   |     5.06371  |       1.06891  |   0.270961 |
| solution-1         |     7.67005  |       1e-06    |   0.604598 |
| solution-2         |     0.524772 |       0.536529 |   0.921557 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.512666 |       0.121672 |   0.294208 |
| solution-flask     |     0.516616 |       1.00883  |   0.299474 |
| solution-aron-mark |     0.51575  |       0.129874 |   0.304204 |
| solution-1-flask   |     0.517361 |       1.00897  |   0.807605 |
| solution-2         |     0.529423 |       0.524717 |   9.01861  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.517627 |       0.130646 |   0.912572 |
| solution-pl        |     0.521068 |       0.129885 |   0.917406 |
| solution-flask     |     0.515706 |       1.00903  |   1.27015  |
| solution-1-flask   |     0.519326 |       1.00875  |   5.78706  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.513804 |       0.157613 |    2.93512 |
| solution-pl        |     0.526657 |       0.162884 |    2.9727  |
| solution-flask     |     0.515296 |       1.00912  |    4.34775 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.517047 |       0.261373 |    17.0529 |
| solution-aron-mark |     0.523319 |       0.263135 |    17.2377 |