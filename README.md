# Domestic Robot Failures (DRF)
Using Online Customer Reviews to Classify, Predict, and Learn about Domestic Robot Failures

## Abstract
There is a knowledge gap regarding which types of failures robots experience in domestic settings and how failures influence customer opinions. We classified 10,072 customer reviews of small utilitarian domestic robots on Amazon.com by the robot failures described in them. We grouped failures into twelve types and three categories (Technical, Interaction, and Service), and analyzed their relations to star rating. Technical failures were more detrimental to customer experience than Interaction or Service failures. Specifically, failures related to Task Completion and Robustness & Resilience were commonly reported in the online reviews and had the greatest negative impact. Hence, failure-prevention and failure-response strategies should address the robot’s technical ability to meet functional goals and maintain operation and structural integrity over time. Usability and user experience are essential but seem to be less detrimental to customer experience. Perhaps customers are more forgiving and tolerant to failures that impact these aspects. Further, we identified sources and types of failures previously overlooked in the literature, combining them into an updated failure taxonomy that merges state of the art on robot failures. In addition, we developed a Natural Language Processing model capable of predicting whether a customer review contains content that describes a failure and the type of failure the review describes. With this knowledge, designers and researchers of robotic systems can prioritize design and development efforts towards essential issues.

## Instructions
Run `0_main.sh`

* This file will invoke the `1_amazonbert.py` python script that will preapear the data for fine-tuning BERT.
* Next, fine-tuning of BERT is performed for the model selected in `1_amazonbert.py`. 
* Finnaly, evaluation of the fine-tuned model is performed using `2_amazonebert_results.py`.

`1_amazonbert.py` 

* Edit the script to select the data for fine-tuning BERT of each of the four tasks to create Model 1 to 4, described in the manuscript. 


`2_amazonebert_results.py`

* This script reads the classifications made by the fine-tuned BERT model and evaluate its performance using F1-score, and the confusion matrix that allows calculating Precision and Recall.


## Contact information
For help or issues using DRF, please submit a GitHub issue.
