# 2024-10-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08225  |       1.0859   |   0.10306  |
| solution-aron-mark |     0.553705 |       0.107138 |   0.188072 |
| solution-pl        |     5.67992  |       0.107877 |   0.192182 |
| solution-1-flask   |     0.567586 |       1.009    |   0.26037  |
| solution-1         |     7.56429  |       1e-06    |   0.591317 |
| solution-2         |     0.552896 |       0.505246 |   0.952233 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.559363 |       0.109866 |   0.295449 |
| solution-pl        |     0.564133 |       0.109194 |   0.33983  |
| solution-flask     |     0.559702 |       1.00896  |   0.474873 |
| solution-1-flask   |     0.555579 |       1.00892  |   0.776996 |
| solution-2         |     0.552842 |       0.469737 |   2.27943  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.558963 |       0.116059 |    1.00438 |
| solution-pl        |     0.559061 |       0.115087 |    1.01025 |
| solution-flask     |     0.557567 |       1.00883  |    2.12538 |
| solution-1-flask   |     0.56425  |       1.00912  |    5.38322 |
| solution-2         |     0.560735 |       0.524802 |   39.0063  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.559733 |       0.143579 |    4.12814 |
| solution-pl        |     0.554221 |       0.146896 |    4.15611 |
| solution-flask     |     0.553288 |       1.00887  |    8.12453 |